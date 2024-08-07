from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from crud_pinturas.views import test

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", test),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
