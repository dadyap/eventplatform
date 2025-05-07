from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_framework.decorators import api_view


@api_view(['GET'])
def hello(request):
    return HttpResponse('Hello, world!')