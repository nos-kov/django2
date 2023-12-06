from django.urls import path
from .views import DemoView, Measurement, Sensor_get

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    #path('sensors/<str:name>/<str:descr>/', new_sensor, name='new_sensor'),
    path('sensors/', DemoView.as_view(), name='new_sensor'),
    path('measurements/', Measurement.as_view(), name='new_measurements'),
    path('sensors/<int:id>/', Sensor_get.as_view(), name='get_sensor'),
]
