from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EmailMessageForm
from .models import EmailMessage
from ai_core.run_pipeline import process_email
import asyncio

def smart_reply_home(req):
    return render(req, 'smart_reply/home.html')

def smart_reply_view(request):
    if request.method == "POST":
        form = EmailMessageForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.save()

            if email.text is None:
                email.text = ""
            
            file_path = email.file.path if email.file else None

            result = asyncio.run(process_email(
                text=email.text,
                file_path=file_path
            ))

            email.category = result.get("category")
            email.ai_response = result.get("ai_response")
            email.save()
            
            context = {
                "ai_response": email.ai_response,
                "category": email.category
            }

            return redirect("email_detail", email.id)

    else:
        form = EmailMessageForm()

    emails = EmailMessage.objects.order_by("-data_req")[:10]

    return render(request, "smart_reply/forms.html", {
        "form": form,
        "email_list": emails
    })
    

def email_detail(request, pk):
    email = get_object_or_404(EmailMessage, pk=pk)
    return render(request, "smart_reply/email_message_form.html", {
        "form": EmailMessageForm(instance=email),
        "email": email
    })


