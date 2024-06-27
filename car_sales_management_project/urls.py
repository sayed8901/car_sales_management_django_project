from django.contrib import admin
from django.urls import path, include
from . import views

# necessary importing for media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),

    path('brand/<slug:brand_slug>/', views.home, name='brand_wise_car'),

    path('user/', include('user.urls')),
    path('car/', include('car.urls')),
    path('brand_app/', include('brand.urls')),
    path('order/', include('order.urls')),
]

# adding media url to urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
