from django.urls import path
from .views import lookup_student, send_otp, verify_otp

urlpatterns = [
    path('lookup-student/', lookup_student, name='lookup_student'),
    path('send-otp/', send_otp, name='send_otp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
]