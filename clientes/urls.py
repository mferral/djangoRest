from django.urls import path

from . import views

urlpatterns = [
    path('clientes/', views.ClienteList.as_view()),
    path('cliente-list/', views.list_clientes),
    path('cliente-create/', views.create_cliente),
    path('cliente-update/<int:pk>', views.update_cliente),    
]