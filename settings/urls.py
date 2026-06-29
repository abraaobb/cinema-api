from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r"studio", views.StudioViewSet)
router.register(r"movie", views.MovieViewSet)
router.register(r"person", views.PersonViewSet)
router.register(r"movie-person", views.MoviePersonViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(router.urls))]
