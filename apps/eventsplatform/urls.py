from django.urls import path
from .views import hello
from . import views

urlpatterns = [
    path('helo', hello, name='hello'),
]