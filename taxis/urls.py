from django.urls import path
from taxis.views import TaxiApiView

urlpatterns_taxis = [
    path('v1/taxis/', TaxiApiView.as_view()),
]