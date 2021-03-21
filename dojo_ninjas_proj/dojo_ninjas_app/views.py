from django.shortcuts import HttpResponse, redirect, render
from .models import Dojo, Ninja


def index(request):
    dojos = Dojo.objects.all()
    context = {
        "dojos": dojos
    }

    return render(request, "index.html", context)


def dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect("/")


def ninja(request):
    dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo_id=dojo
    )
    return redirect("/")
