from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "index"
urlpatterns = [
    path('', views.index, name="home"),
    path('JhnoisnUHVmks', views.key, name="key"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)