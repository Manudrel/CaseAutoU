from django.urls import path
from .views import smart_reply_view, smart_reply_home, email_detail, smart_reply_tutorial

app_name = "smart_reply"

urlpatterns = [
    path('', smart_reply_home, name='home'),                       
    path('process/', smart_reply_view, name='process'),            
    path('email/<int:pk>/', email_detail, name='detail'),
    path('tutorial/', smart_reply_tutorial, name='tutorial'),          
]
