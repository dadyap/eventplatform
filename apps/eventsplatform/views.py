from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from unicodedata import category
from yaml import serialize

from apps.eventsplatform.models import Event, Category, Ticket
from apps.eventsplatform.serializers import EventSerializer, CategorySerializer, TicketSerializer


@api_view(['GET'])
def hello(request):
    return HttpResponse('Hello, world!')

class CategoryListApiView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class EventListApiView(APIView):
    def get(self, request):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

class TicketListApiView(APIView):
    def get(self,request):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)