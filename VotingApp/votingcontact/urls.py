from django.contrib import admin
from django.urls import include, path
from votingcontact import views

urlpatterns = [
  path('', views.contact, name='contact'),
]