from django.shortcuts import render
import logging
from rest_framework.pagination import  PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from trajectories.models import Trajectories
from trajectories.serializers import TrajectoriesSerializer
from django.db.models import Max


# Configuración de los logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TrajectoriesApiView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request, taxi_id=None, date=None):
        logger.debug("Recibida solicitud GET")

        if not date:
            logger.error("Fecha no proporcionada en la solicitud")
            return Response({"error": "Se requiere una fecha"}, status=status.HTTP_400_BAD_REQUEST)

        logger.debug(f"Fecha proporcionada: {date}")

        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            logger.error("Formato de fecha incorrecto en la solicitud")
            return Response({"error": "Formato de fecha incorrecto. Utilice el formato 'YYYY-MM-DD'"}, status=status.HTTP_400_BAD_REQUEST)

        logger.debug(f"Fecha convertida a objeto datetime: {date_obj}")

        if taxi_id is None:
            logger.error("ID de taxi no proporcionado en la solicitud")
            return Response({"error": "Se requiere un ID de taxi"}, status=status.HTTP_400_BAD_REQUEST)

        logger.debug(f"ID de taxi proporcionado: {taxi_id}")

        trajectories = Trajectories.objects.filter(taxi_id=taxi_id, date=date_obj)

        logger.debug(f"Consultando base de datos para ID de taxi {taxi_id} en la fecha {date_obj}")

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(trajectories, request)
        serializer = TrajectoriesSerializer(result_page, many=True)

        logger.debug("Respuesta exitosa")
        return paginator.get_paginated_response(serializer.data)
        
class LastLocationApiView(APIView):
    pagination_class = PageNumberPagination

    def get(self,request):
        last_trajectorie = Trajectories.objects.values('taxi_id').annotate(max_date=Max('date')).order_by('taxi_id') #Lista de mayor a menor en base a la fecha

        trajectories = [Trajectories.objects.filter(taxi_id=item['taxi_id'], date=item['max_date']).first() for item in last_trajectorie]
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(trajectories,request)
        serializer = TrajectoriesSerializer(result_page, many = True)
        return paginator.get_paginated_response(serializer.data)
