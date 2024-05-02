

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Customer
import datetime


def send_email():
    today = datetime.date.today()
    customerData = Customer.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month)
    for customer in customerData:
        context = {
            "receiver_name": customer.name,
            "age": calculateAge(customer.date_of_birth),
            "year": 2024
        }
        template_name = "email.html"
        convert_to_html_content =  render_to_string(
            template_name = template_name,
            context = context
        )    
        message = EmailMultiAlternatives(
            subject='Happy Birthday to '+ customer.name,
            body="Wishing Happy birthday to your birthday. Many Many happy return of the day.",
            from_email = settings.EMAIL_HOST_USER,
            to=[customer.email]
        )
        message.attach_alternative(convert_to_html_content, "text/html")
        message.send(fail_silently=False)

def calculateAge(birthDate):
    today = datetime.date.today()
    year = int(birthDate.strftime("%Y"))
    month = int(birthDate.strftime("%m"))
    day = int(birthDate.strftime("%d"))
    age = today.year - year - ((today.month, today.day) < (month, day)) 
    return age