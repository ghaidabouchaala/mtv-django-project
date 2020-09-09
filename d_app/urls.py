from django.urls import path
from d_app import views

urlpatterns = [
    path('', views.index)
]