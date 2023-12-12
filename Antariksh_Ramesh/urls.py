# Contact_details/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='contacts/', permanent=False)),
    path('contacts/', include('Contact_details.urls')),
]