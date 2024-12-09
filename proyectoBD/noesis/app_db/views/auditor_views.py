from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from app_db.models import Producto, Inventario, OrdenDistribuidor, DetalleOrden, Empleado, Distribuidor

# Producto
@permission_required('app_db.view_producto', raise_exception=True)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'auditor/producto_list.html', {'productos': productos})

# Inventario
@permission_required('app_db.view_inventario', raise_exception=True)
def inventario_list(request):
    inventarios = Inventario.objects.all()
    return render(request, 'auditor/inventario_list.html', {'inventarios': inventarios})

# OrdenDistribuidor
@permission_required('app_db.view_ordendistribuidor', raise_exception=True)
def orden_distribuidor_list(request):
    ordenes = OrdenDistribuidor.objects.all()
    return render(request, 'auditor/orden_distribuidor_list.html', {'ordenes': ordenes})

# DetalleOrden
@permission_required('app_db.view_detalleorden', raise_exception=True)
def detalle_orden_list(request):
    detalles = DetalleOrden.objects.all()
    return render(request, 'auditor/detalle_orden_list.html', {'detalles': detalles})

# Empleado
@permission_required('app_db.view_empleado', raise_exception=True)
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'auditor/empleado_list.html', {'empleados': empleados})

# Distribuidor
@permission_required('app_db.view_distribuidor', raise_exception=True)
def distribuidor_list(request):
    distribuidores = Distribuidor.objects.all()
    return render(request, 'auditor/distribuidor_list.html', {'distribuidores': distribuidores})

@login_required
def auditor_dashboard(request):
    return render(request, 'auditor/dashboard.html')