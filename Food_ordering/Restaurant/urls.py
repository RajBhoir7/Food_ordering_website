"""
URL configuration for Food_ordering project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from Restaurant import views
#Restaurant urls
urlpatterns = [
    path('Register_Restaurant/',views.Register_Restaurant.as_view(),name='Register_Restaurant'),
    path('Rest_login/',views.Rest_login.as_view(),name='Rest_login'),
    path('Restaurant_main/',views.Rest_home.as_view(),name='Restaurant_main'),
    path('add_Food/',views.Add_Food,name='add_Food'),
    path('RestaurantFood/',views.RestaurantFood.as_view(),name='RestaurantFood'),
    

    path('admin/', admin.site.urls),
]
