from django.shortcuts import HttpResponse, redirect, render
from .models import User


def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "index.html", context)


def user_create(request):
    new_user = User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_name=request.POST['email_name'], age=request.POST['age'])
    new_user.save()

    return redirect('/')
