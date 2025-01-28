from django.contrib import admin
from django.urls import path, include
from wish import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wish/", include("wish.urls")),
    path("common/", include("common.urls")),
    path("", views.main, name="main"),
]
