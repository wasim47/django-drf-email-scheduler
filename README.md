# django-drf-email-scheduler
Using apscheduler for DRF to send customers automatically birthday wishes notifications by mail

# Project Setup
1. install the latest version of Python and Django
2. Install Django rest framework by following DRF documentation: 
  https://www.django-rest-framework.org/#requirements
3. After successful installation you need to make migration with this command
    **pip manage.py makemigrations**  # To make migration for all tables
    **pip manage.py migrate**         # Trigger migrate according to migration

   Now you need to create a super user to access django admin.
   **py manage.py createsuperuser**
   Ener your username: 
   Enter Email address:
   Enter password:
   Ener Password (again):

    Then you can log in Django admin by using the above credentials
5. Now the project is successfully installed

Now you will find a restapp in your project with restapi folder also.
Here 4 files contain customer data insert/update/delete and list view (CRUD Operation)
You can run on your project restapi files to get list and create/update/delete customer data also

  **py .\restapi\list.py** 
  **py .\restapi\create.py** 
  **py .\restapi\update.py** 
  **py .\restapi\delete.py** 

You can also run by using postman or other apps to read API.
You can also crud operation by using django admin.


# You also need to install apschedule if not available on your project

pip install django-apscheduler
In the scheduler already cron time set. Cron will run every day first minute of 00 hour

**scheduler.add_job(send_email, 'cron', day='*', hour=0, minute=1)**

You can modify it as you need also


# Email Configuration

Now for sending mail, you need to set your email credentials by using SMTP in the settings.py file
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_POTRT = 587
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'app password for your Gmail accoung'
EMAIL_FROM_USER = 'example@gmail.com'


Finally customer will get birthday wishing email on there birthday.
   
