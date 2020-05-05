from django.contrib import admin
from django.urls import path
from . import views

app_name = "homework"
urlpatterns = [
    path('dashboard/',views.dashboard, name = "dashboard"),
    path('addhomework/',views.addhomework, name = "addhomework"),
    path('',views.userhomeworks,name = "userhomeworks"),
    path('homework/<int:id>',views.detail,name = "detail"),
    path('delete/<int:id>',views.delete,name = "delete"),
    path('update/<int:id>',views.update,name = "update"),
    path('userupdate/<int:id>',views.userupdate,name = "userupdate"),
    

]