from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/<int:candidate_id>/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
    path('login/', views.custom_login, name='login'),
    path('chatbot/', views.chatbot, name='chatbot'),
]