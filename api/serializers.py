from rest_framework import serializers
from .models import IpoInfo

class IpoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpoInfo
        fields = '__all__'