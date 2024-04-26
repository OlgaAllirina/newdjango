from rest_framework import serializers

from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.Serializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementSerializer(serializers.Serializer):

    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temperature', 'created_at', 'image']
