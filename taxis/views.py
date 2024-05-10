from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from taxis.models import Taxi
from taxis.serializers import TaxiSerializer
from rest_framework.pagination import  PageNumberPagination

class TaxiApiView(APIView):
     pagination_class = PageNumberPagination

     def get(self, request):
        taxis = Taxi.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(taxis, request)
        serializer = TaxiSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
       

     
