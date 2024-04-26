from django.contrib import admin
from measurement.models import Sensor, Measurement


# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurement)
class Measurement(admin.ModelAdmin):
    pass