# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class SensorsSerializer:
    pass


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        data = SensorsSerializer(sensors, many=True).data
        return Response(data)

    def post(self, request, sensor_name, sensor_description):
        sensor = Sensor.objects.create(name=sensor_name, description=sensor_description)
        sensor.save()
        data = SensorsSerializer(sensor).data
        return Response(data)

    def patch(self, request, sensor_id, sensor_description):
        sensor = Sensor.objects.get(id=sensor_id)
        sensor.description = sensor_description
        sensor.save()
        data = SensorsSerializer(sensor).data
        return Response(data)


class MeasurementView(APIView):
    def post(self, request, sensor_id, temp_value):
        sensor = Sensor.objects.get(id=sensor_id)
        measurement = Measurement.objects.create(sensor_id=sensor, temperature=float(temp_value))
        measurement.save()
        data = MeasurementSerializer(measurement).data
        return Response(data)

    def get(self, request, sensor_id):
        measurements = Measurement.objects.filter(sensor_id=sensor_id)
        data = MeasurementSerializer(measurements, many=True).data
        return Response(data)

    def post(self, request):
        return Response({'status': 'OK'})
