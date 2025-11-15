from django.urls import path
from .views import smart_reply_view, smart_reply_home, email_detail

urlpatterns = [
    path('', smart_reply_home, name='smart_reply_home'),
    path('smart_reply/', smart_reply_view, name='smart_reply'),
    path('<int:pk>/', email_detail, name='email_detail'),
]
