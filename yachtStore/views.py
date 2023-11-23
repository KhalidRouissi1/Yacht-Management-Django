from django.shortcuts import render
from django.http import HttpRequest
def index(req):
    return HttpRequest("Hi form yacht app⛵!!")