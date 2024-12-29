from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dotenv import load_dotenv
import os

load_dotenv()
admin_url = os.getenv("ADMIN_PAGE")  

urlpatterns = [
    path(admin_url, admin.site.urls), 
    path("psinous_app/", include("psinous_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
