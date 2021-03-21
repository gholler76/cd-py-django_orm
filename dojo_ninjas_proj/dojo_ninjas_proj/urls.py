from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('dojo_ninjas_app.routes')),

]
