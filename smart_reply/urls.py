from django.urls import path
from .views import smart_reply_view, smart_reply_home

urlpatterns = [
    path('', smart_reply_home),
    path('smart_reply/', smart_reply_view),
]
