from django.urls import path
from .views import hello, EventListApiView, CategoryListApiView, TicketListApiView
from . import views

urlpatterns = [
    path('hello', hello, name='hello'),
    path('events/', EventListApiView.as_view(), name='events-list'),
    path('category/', CategoryListApiView.as_view(), name='category-list'),
    path('ticket/', TicketListApiView.as_view(), name='ticket-list'),
]