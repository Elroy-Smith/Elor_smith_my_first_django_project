"""django_first_project URL Configuration

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
from django.urls import path, include

import django_first_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', django_first_app.views.index),
    path('hello/', django_first_app.views.hello),
    path('game/', django_first_app.views.game),
    path('article/<int:id>', django_first_app.views.article),
    path('product/', django_first_app.views.show_products),
    path('product/add/', django_first_app.views.form),
    # path('book/add/', django_first_app.views.BookAddView.as_view()),
    # path('book/', django_first_app.views.show_all_books),
    path('book/', include('django_first_app.urls')),
    path('fizzbuzz/', django_first_app.views.fizz_buzz),
]
