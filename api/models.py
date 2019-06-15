from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)

    @property
    def temperature(self):
        return Temperature.objects.filter(client=self).order_by('-datetime')[:10]

    @property
    def humidity(self):
        return Humidity.objects.filter(client=self).order_by('-datetime')[:10]


class Temperature(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    value = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)


class Humidity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    value = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
