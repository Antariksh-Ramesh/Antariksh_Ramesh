# Contact_details/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .views import contact_list, contact_create, contact_update, contact_delete


urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('create/', contact_create, name='contact_create'),
    path('<int:pk>/update/', contact_update, name='contact_update'),
    path('<int:pk>/delete/', contact_delete, name='contact_delete'),
]
