"""sewamobilmysql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from mobilmysql import views
from mobilmysql import carviews
from mobilmysql import rentviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.IndexView.as_view(), name='index'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='detail'),
    path('contacts/edit/<int:pk>/', views.edit, name='edit'),
    path('contacts/detail/<int:pk>/', views.detail, name='detail'),
    path('contacts/create/', views.create, name='create'),
    path('contacts/delete/<int:pk>/', views.delete, name='delete'),

    path('cars/', carviews.IndexView.as_view(), name='carsindex'),
    path('cars/<int:pk>/', carviews.CarDetailView.as_view(), name='carsdetail'),
    path('cars/edit/<int:pk>/', carviews.edit, name='carsedit'),
    path('cars/detail/<int:pk>/', carviews.detail, name='carsdetail'),
    path('cars/create/', carviews.create, name='carscreate'),
    path('cars/delete/<int:pk>/', carviews.delete, name='carsdelete'),

    path('rent/', rentviews.IndexView.as_view(), name='rentindex'),
    path('rent/<int:pk>/', rentviews.RentDetailView.as_view(), name='rentdetail'),
    path('rent/edit/<int:pk>/', rentviews.edit, name='rentedit'),
    path('rent/detail/<int:pk>/', rentviews.detail, name='rentdetail'),
    path('rent/create/', rentviews.create, name='rentcreate'),
    path('rent/delete/<int:pk>/', rentviews.delete, name='rentdelete'),
]
