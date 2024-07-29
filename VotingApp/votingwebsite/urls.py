from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    #  path('home/', views.next_page, name='next_page'),
    path('home/', views.home, name='home'),
     path('election/<int:election_id>/', views.election_detail, name='election_detail'),
    path('election/<int:election_id>/vote/<int:candidate_id>/', views.vote, name='vote'),
    # Add other URL patterns for other functionalities if needed
]
