from django.urls import path
from . import views


urlpatterns = [
    path('Wrlcome/', views.Welcome, name='Welcome'),
    path('', views.Template, name='Template'),
    path('dashboard/', views.Dashboard, name='dash'),
    path('details/', views.details, name='details'),
]