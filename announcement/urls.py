from django.contrib import admin
from django.urls import path
from . import views

app_name = "announcement"
urlpatterns = [
    path('',views.announcement,name="announcement"),
    path('addannouncement/',views.addannouncement,name="addannoncement")
]