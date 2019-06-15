from django.shortcuts import render

from api.models import Client


def dashboard(request):
    """A view of all bands."""
    clients = Client.objects.all()
    return render(request, 'dashboard.html', {'clients': clients})
