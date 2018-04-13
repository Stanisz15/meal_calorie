"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from diet.views import StartPageView, UserLoginView, UserLogoutView, NewUserView, AddProductView, UpdateProductView, \
    ProductsView, ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', StartPageView.as_view(), name='main'),
    url(r'^login$', UserLoginView.as_view(), name='login'),
    url(r'^logout$', UserLogoutView.as_view(), name='logout'),
    url(r'^add_user$', NewUserView.as_view(), name='register'),
    url(r'^add_product$', AddProductView.as_view(), name='add-product'),
    url(r'^update_product/(?P<pk>\d+)/$', UpdateProductView.as_view(), name='update-product'),
    url(r'^products', ProductsView.as_view(), name="products"),
    url(r'^product/(?P<product_id>(\d)+)', ProductView.as_view(), name='product'),
]