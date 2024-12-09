from django.urls import path
from app_db.views import auditor_views  # type: ignore

urlpatterns = [
    # Producto
    path('productos/', auditor_views.producto_list, name='auditor_producto_list'),

    # Inventario
    path('inventarios/', auditor_views.inventario_list, name='auditor_inventario_list'),

    # Empleado
    path('empleados/', auditor_views.empleado_list, name='auditor_empleado_list'),

    # Distribuidor
    path('distribuidores/', auditor_views.distribuidor_list, name='auditor_distribuidor_list'),

    # OrdenDistribuidor
    path('ordenes/', auditor_views.orden_distribuidor_list, name='auditor_orden_distribuidor_list'),

    # DetalleOrden
    path('detalles/', auditor_views.detalle_orden_list, name='auditor_detalle_orden_list'),

    # Dashboard
    path('dashboard/', auditor_views.auditor_dashboard, name='auditor_dashboard'),

    path('dashboard/', auditor_views.auditor_dashboard, name='auditor_dashboard'),

]
