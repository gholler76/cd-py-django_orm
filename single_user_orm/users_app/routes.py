from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('user_create', views.user_create)

]
