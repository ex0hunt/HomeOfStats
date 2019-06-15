from django.conf.urls import url
from api.views import ClientsView, ClientDetailView, TemperatureView, HumidityView

urlpatterns = [
    url(r'^clients/$', ClientsView.as_view()),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailView.as_view()),
    url(r'^sensors/temp/$', TemperatureView.as_view()),
    url(r'^sensors/humid/$', HumidityView.as_view()),
]
