from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from datetime import datetime

def index(request):
    # return HttpResponse("<h1>Hello</h1>")
    # return redirect(reverse('admin:index'))

    # return JsonResponse(dict(hello="world"))
    context = {
        "first_name": "Elnur",
        "date": datetime.now()
    }
    return render(request, "index.html", context)
