from django.urls import path
from . import views

urlpatterns = [
    path('Wrlcome/', views.Welcome, name='Welcome'),
    path('', views.Template, name='Template'),
]