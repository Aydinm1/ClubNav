from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'club', views.ClubViewSet, basename='Club')

app_name = "list"
urlpatterns = [
    path('', include(router.urls)),
    path('<int:club_id>/', views.clubtemplate, name = 'club-template'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)