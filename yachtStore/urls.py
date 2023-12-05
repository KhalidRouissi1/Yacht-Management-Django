    
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addyacht',views.add,name="add"),
    path('edit/<int:id>',views.editYacht,name="edit"),
    path('buy/<int:yid>',views.getById,name='getById'),
    path('buy',views.show,name='buy'),
    path('delete/<int:id>',views.delete,name='delete'),

    
]
