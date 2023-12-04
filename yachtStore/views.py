from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def index(req):
    return render(req,"index.html")

@login_required
def buyYacht(req):
    return render(req,"store/index.html")