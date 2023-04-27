from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "list"
urlpatterns = [
    path('', views.index),
    path('<int:club_id>/', views.clubtemplate, name = 'club-template'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)