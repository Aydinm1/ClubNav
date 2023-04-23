from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('club-template/', views.clubtemplate, name = 'club-template')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)