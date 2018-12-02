"""exercises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from zjazd_5.django_examples.exercises.mainpage.views import main_page, hello_world, hello_personalized, dodaj
from zjazd_5.django_examples.exercises.maths.views import math_operations

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page),
    path("hello", hello_world),
    path("hello/<name>/<lastname>", hello_personalized),
    path("calc/<a>/<b>", dodaj),
    path("maths/<operation>/<int:arg_a>/<int:arg_b>", math_operations),
]
