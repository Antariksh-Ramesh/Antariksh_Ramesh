# Contact_details/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .views import contact_list, contact_create, contact_update, contact_delete
from Contact_details import views

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/<int:pk>/update/', contact_update, name='contact_update'),
    path('contacts/<int:pk>/delete/', contact_delete, name='contact_delete'),
]
