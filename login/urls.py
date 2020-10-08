from django.urls import path
from .views import *

urlpatterns = [
    path('login', getform, name='get_login_form'),
    path('login/verify', verifylogin, name='verify_login_details')
]