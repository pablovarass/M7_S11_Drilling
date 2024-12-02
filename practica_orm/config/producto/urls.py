from django.urls import path
from .views import listar, crear, editar, eliminar_producto, index, buscar, mostrar_cadena, detalle_producto, crearusuario, iniciar_sesion, cerrar_sesion
urlpatterns = [
    path('', index, name='index'),
    path('listar_producto/', listar, name='listar_producto'),
    path('crear_producto/', crear, name='crear_producto'),
    path('editar_producto/<int:producto_id>', editar, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>', eliminar_producto, name='eliminar_producto'),
    path('buscar/', buscar, name='buscar'),
    path('producto/username/<str:cadena>/', mostrar_cadena, name='mostrar_cadena'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('usuario/registro/', crearusuario, name='registro'),
    path('crearusuario/', crearusuario, name='crearusuario'),
    path('login/', iniciar_sesion, name='login'),  
    path('logout/', cerrar_sesion, name='logout'),
    ]
