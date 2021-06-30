from django.urls import path
from .views import index,Colab

urlpatterns = [
    path('', index,name="index"),
    path('Colab',Colab,name='Colab'),
]