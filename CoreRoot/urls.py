from django.conf.urls.static import static 
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path("", index, name="landing"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
