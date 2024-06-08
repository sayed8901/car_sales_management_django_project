from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('user/', include('user.urls')),
    path('car/', include('car.urls')),
    path('brand/', include('brand.urls')),
]
