# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from rest_framework import status


class DemoView(APIView):
    
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many = True)
        return Response(ser.data)

    def post(self,request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Measurement(APIView):
    
    def post(self,request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sensor_get(APIView):

    def get(self, request, id):
        sensors = Sensor.objects.filter(id=id)
        ser = SensorDetailSerializer(sensors, many = True)
        return Response(ser.data)
    
    def patch(self, request, id):
        instance = Sensor.objects.get(id=id)
        serializer = SensorSerializer(instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
