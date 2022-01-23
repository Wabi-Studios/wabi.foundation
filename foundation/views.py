from django.shortcuts import render
from django.http import HttpResponse

import darkdetect


def index(request):
    return render(request, "index.html")

