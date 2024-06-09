from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddCarView.as_view(), name='add_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car_info'),
    
    path('buy/<int:id>/<str:username>/', views.car_buy, name='car_buy'),
]
