"""
URL configuration for birthdayWithingEmail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('customer-list/', views.customer_list, name="customerlist"),
    path('customer/<int:pk>', views.customer, name="customerinfo"),
    path('customer-register/', views.customer_create, name="customercreate"),
    path('customer-update/', views.customer_update, name='customerupdate'),
    path('customer-delete/', views.customer_delete, name='customerdelete'),
]
