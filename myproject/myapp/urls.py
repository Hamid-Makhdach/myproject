from django.contrib import admin
from django.urls import path
from .views import PredictionView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('result/', PredictionView.as_view(), name='result'),

]
