from django.urls import path
from . import views

app_name = "wish"

urlpatterns = [
    path("main/", views.main, name="main"),
]
