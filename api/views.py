from rest_framework import generics

from api.models import Client, Temperature, Humidity
from api.serializers import ClientSerializer, ClientItemSerializer, TemperatureItemSerializer, HumidityItemSerializer


class ClientsView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientItemSerializer


class TemperatureView(generics.ListCreateAPIView):
    queryset = Temperature.objects.all().order_by('-datetime')
    serializer_class = TemperatureItemSerializer


class HumidityView(generics.ListCreateAPIView):
    queryset = Humidity.objects.all().order_by('-datetime')
    serializer_class = HumidityItemSerializer
