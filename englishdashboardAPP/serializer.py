from rest_framework import serializers
from .models import Expressao



class ExpressaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expressao
        # fields = ['id','name'] 
        # como puxar todos os campos
        fields = '__all__'
