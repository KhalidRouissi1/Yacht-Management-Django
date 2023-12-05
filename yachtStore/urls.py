    
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('buy',views.shOwYachts,name="buy"),
    path('add',views.shOwYachts,name="add"),
    path('edit',views.editYacht,name="edit"),
    
]
