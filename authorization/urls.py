from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.AuthToken.as_view()),
    path('logout/', views.RemoveToken.as_view()), 
]