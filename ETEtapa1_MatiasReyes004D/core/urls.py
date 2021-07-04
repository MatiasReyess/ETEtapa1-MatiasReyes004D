from django.urls import path
from .views import index,Colab,agregar,modificar,eliminar
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index,name="index"),
    path('Colab',Colab,name='Colab'),
    path('ingresar',agregar,name='ingresar'),
    path('modificar/<id>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar,name="eliminar"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
