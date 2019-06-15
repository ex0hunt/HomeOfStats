from rest_framework import serializers

from api.models import Client, Temperature, Humidity


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']


class ClientItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['value', 'datetime']


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['value', 'datetime']


class TemperatureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'


class HumidityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = '__all__'
