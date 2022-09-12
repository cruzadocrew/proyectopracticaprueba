"""PracticaPrueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app2 import views as app2
from app1 import views as app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1view2app/',app2.display3 ),
    path('2view2app/',app2.display4),
    path('1view1app/',app1.display1),
    path('2view1app/',app1.display2),
]