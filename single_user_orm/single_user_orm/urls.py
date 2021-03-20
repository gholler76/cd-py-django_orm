from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('users_app.routes')),
    path('user_create', include('users_app.routes')),

]
