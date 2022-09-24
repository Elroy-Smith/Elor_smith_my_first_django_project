from django.urls import path

import django_first_app

urlpatterns = [
    path('', django_first_app.views.show_all_books ),
    path('add/', django_first_app.views.BookAddView.as_view() ),
]