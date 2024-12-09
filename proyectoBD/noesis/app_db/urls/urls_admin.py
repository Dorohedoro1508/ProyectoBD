from django.urls import path
from app_db.views import admin_views  # type: ignore

urlpatterns = [
    path('dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('productos/', admin_views.producto_list, name='admin_producto_list'),
    path('productos/agregar/', admin_views.producto_create, name='admin_producto_create'),
    path('productos/editar/<int:pk>/', admin_views.producto_update, name='admin_producto_update'),
    path('productos/eliminar/<int:pk>/', admin_views.producto_delete, name='admin_producto_delete'),
    path('inventarios/', admin_views.inventario_list, name='admin_inventario_list'),
    path('inventarios/agregar/', admin_views.inventario_create, name='admin_inventario_create'),
    path('inventarios/editar/<int:pk>/', admin_views.inventario_update, name='admin_inventario_update'),
    path('inventarios/eliminar/<int:pk>/', admin_views.inventario_delete, name='admin_inventario_delete'),
    path('empleados/', admin_views.empleado_list, name='admin_empleado_list'),
    path('empleados/agregar/', admin_views.empleado_create, name='admin_empleado_create'),
    path('empleados/editar/<int:pk>/', admin_views.empleado_update, name='admin_empleado_update'),
    path('empleados/eliminar/<int:pk>/', admin_views.empleado_delete, name='admin_empleado_delete'),
    path('distribuidores/', admin_views.distribuidor_list, name='admin_distribuidor_list'),
    path('distribuidores/agregar/', admin_views.distribuidor_create, name='admin_distribuidor_create'),
    path('distribuidores/editar/<int:pk>/', admin_views.distribuidor_update, name='admin_distribuidor_update'),
    path('distribuidores/eliminar/<int:pk>/', admin_views.distribuidor_delete, name='admin_distribuidor_delete'),
    path('ordendistribuidor/', admin_views.orden_distribuidor_list, name='admin_ordendistribuidor_list'),
    path('ordendistribuidor/agregar/', admin_views.orden_distribuidor_create, name='admin_ordendistribuidor_add'),
    path('ordendistribuidor/<int:id_ord>/editar/', admin_views.orden_distribuidor_edit, name='admin_ordendistribuidor_edit'),
    path('ordendistribuidor/<int:id_ord>/eliminar/', admin_views.orden_distribuidor_delete, name='admin_ordendistribuidor_delete'),
    path('respaldos/descargar/', admin_views.descargar_respaldo, name='descargar_respaldo'),
    path('respaldos/subir/', admin_views.subir_respaldo, name='subir_respaldo'),
    path('detalleorden/', admin_views.detalle_orden_list, name='admin_detalleorden_list'),
    path('detalleorden/agregar/', admin_views.detalle_orden_create, name='admin_detalleorden_add'),
    path('detalleorden/<int:id_det>/editar/', admin_views.detalle_orden_edit, name='admin_detalleorden_edit'),
    path('detalleorden/<int:id_det>/eliminar/', admin_views.detalle_orden_delete, name='admin_detalleorden_delete'),
    ]

