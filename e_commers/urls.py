"""e_commers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store.views import store_view,cart_view,checkout_view

urlpatterns = [

	path('',store_view ,name = 'store_view'),
	path('cart/',cart_view,name = 'cart_view'),
	path('checkout/',checkout_view ,name = 'checkout_view'),

    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)