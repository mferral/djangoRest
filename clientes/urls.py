from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('clientes/', views.ClienteList.as_view()),
    path('cliente-list/', views.list_clientes),
    path('cliente-create/', views.create_cliente),
    path('cliente-update/<int:pk>', views.update_cliente),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)