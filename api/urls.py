from django.urls import path
from . import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define the Swagger schema 
schema_view = get_schema_view(
    openapi.Info(
        title="Yacht Store API",
        default_version='v0.1',
        description="An api from our store to use it in our sub-companies to use the CRUD functionality in their app using our Cetrelized DataBase",
        terms_of_service="Nothing For Now",
        contact=openapi.Contact(email="khalidrouissi7@gmail.com & dorransir24@gmail.com"),
        license=openapi.License(name="MIT Licence"),
    ),
    public=True,
)

urlpatterns = [
    path("", views.getData, name="get-data"),
    path("add", views.addItem, name="add-item"),
    path("edit/<int:pk>", views.editItem, name="edit-item"),
    path("delete/<int:pk>", views.deleteItem, name="delete-item"),

    # Swagger documentation endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
