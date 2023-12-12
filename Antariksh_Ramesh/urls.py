# Antariksh_Ramesh/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from Contact_details.views import contact_list, contact_create, contact_update, contact_delete  # Update this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='contacts/', permanent=False)),
    path('', include('Contact_details.urls')),
    #path('contacts/', include('contacts.urls'))
]

