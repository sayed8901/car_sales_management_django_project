from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.add_car, name='add_car'),
    path('add/', views.AddCarView.as_view(), name='add_car'),
]
