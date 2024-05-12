from django.contrib import admin
from django.urls import include, path
from image_app import views
urlpatterns = [
    path('process/<int:tab_id>/', views.process_image, name='process_image'),
]