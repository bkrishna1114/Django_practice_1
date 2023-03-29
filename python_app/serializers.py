from . models import conn
from rest_framework import serializers


class serial(serializers.ModelSerializer):
    class Meta:
        model = conn
        fields = '__all__'