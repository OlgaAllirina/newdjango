from django.urls import path

from school.views import students_list
from django.contrib import admin

urlpatterns = [
    path('', students_list, name='students'),
    path('admin/', admin.site.urls)
]
