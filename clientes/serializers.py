from .models import Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.CharField(source='get_nombre_completo',required=False,)
    class Meta:
        model = Cliente
        fields = '__all__'
        
class ClientePostSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Cliente
        fields = '__all__'


class ClientePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        # read_only_fields = ('nombre', )
        fields = ['nombre', 'apellido', 'foto']