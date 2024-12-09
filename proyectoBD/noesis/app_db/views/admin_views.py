from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from app_db.models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden
from app_db.forms import ProductoForm, InventarioForm, EmpleadoForm, DistribuidorForm, OrdenDistribuidorForm, DetalleOrdenForm

# Producto
@permission_required('app_db.view_producto', raise_exception=True)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'admin/producto_list.html', {'productos': productos})

@permission_required('app_db.add_producto', raise_exception=True)
def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_producto_list')
    else:
        form = ProductoForm()
    return render(request, 'admin/producto_form.html', {'form': form})

@permission_required('app_db.change_producto', raise_exception=True)
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('admin_producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'admin/producto_form.html', {'form': form})

@permission_required('app_db.delete_producto', raise_exception=True)
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('admin_producto_list')
    return render(request, 'admin/producto_confirm_delete.html', {'producto': producto})


# Inventario
@permission_required('app_db.view_inventario', raise_exception=True)
def inventario_list(request):
    inventarios = Inventario.objects.all()
    return render(request, 'admin/inventario_list.html', {'inventarios': inventarios})

@permission_required('app_db.add_inventario', raise_exception=True)
def inventario_create(request):
    if request.method == "POST":
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_inventario_list')
    else:
        form = InventarioForm()
    return render(request, 'admin/inventario_form.html', {'form': form})

@permission_required('app_db.change_inventario', raise_exception=True)
def inventario_update(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('admin_inventario_list')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'admin/inventario_form.html', {'form': form})

@permission_required('app_db.delete_inventario', raise_exception=True)
def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        inventario.delete()
        return redirect('admin_inventario_list')
    return render(request, 'admin/inventario_confirm_delete.html', {'inventario': inventario})

# Empleado
@permission_required('app_db.view_empleado', raise_exception=True)
def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'admin/empleado_list.html', {'empleados': empleados})

@permission_required('app_db.add_empleado', raise_exception=True)
def empleado_create(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'admin/empleado_form.html', {'form': form})

@permission_required('app_db.change_empleado', raise_exception=True)
def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('admin_empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'admin/empleado_form.html', {'form': form})

@permission_required('app_db.delete_empleado', raise_exception=True)
def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        empleado.delete()
        return redirect('admin_empleado_list')
    return render(request, 'admin/empleado_confirm_delete.html', {'empleado': empleado})

# Distribuidor
@permission_required('app_db.view_distribuidor', raise_exception=True)
def distribuidor_list(request):
    distribuidores = Distribuidor.objects.all()
    return render(request, 'admin/distribuidor_list.html', {'distribuidores': distribuidores})

@permission_required('app_db.add_distribuidor', raise_exception=True)
def distribuidor_create(request):
    if request.method == "POST":
        form = DistribuidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_distribuidor_list')
    else:
        form = DistribuidorForm()
    return render(request, 'admin/distribuidor_form.html', {'form': form})

@permission_required('app_db.change_distribuidor', raise_exception=True)
def distribuidor_update(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    if request.method == "POST":
        form = DistribuidorForm(request.POST, instance=distribuidor)
        if form.is_valid():
            form.save()
            return redirect('admin_distribuidor_list')
    else:
        form = DistribuidorForm(instance=distribuidor)
    return render(request, 'admin/distribuidor_form.html', {'form': form})

@permission_required('app_db.delete_distribuidor', raise_exception=True)
def distribuidor_delete(request, pk):
    distribuidor = get_object_or_404(Distribuidor, pk=pk)
    if request.method == "POST":
        distribuidor.delete()
        return redirect('admin_distribuidor_list')
    return render(request, 'admin/distribuidor_confirm_delete.html', {'distribuidor': distribuidor})

# OrdenDistribuidor
# Listar OrdenDistribuidor
@login_required
def orden_distribuidor_list(request):
    ordenes = OrdenDistribuidor.objects.all()
    return render(request, 'admin/orden_distribuidor_list.html', {'ordenes': ordenes})

# Crear OrdenDistribuidor
@login_required
def orden_distribuidor_create(request):
    if request.method == 'POST':
        form = OrdenDistribuidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_orden_distribuidor_list')
    else:
        form = OrdenDistribuidorForm()
    return render(request, 'admin/orden_distribuidor_form.html', {'form': form})

# Editar OrdenDistribuidor
@login_required
def orden_distribuidor_edit(request, id_ord):
    orden = get_object_or_404(OrdenDistribuidor, id_ord=id_ord)
    if request.method == 'POST':
        form = OrdenDistribuidorForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('admin_orden_distribuidor_list')
    else:
        form = OrdenDistribuidorForm(instance=orden)
    return render(request, 'admin/orden_distribuidor_form.html', {'form': form})

# Eliminar OrdenDistribuidor
@login_required
def orden_distribuidor_delete(request, id_ord):
    orden = get_object_or_404(OrdenDistribuidor, id_ord=id_ord)
    if request.method == 'POST':
        orden.delete()
        return redirect('admin_orden_distribuidor_list')
    return render(request, 'admin/orden_distribuidor_confirm_delete.html', {'orden': orden})

# Listar Detalles de Orden
@login_required
def detalle_orden_list(request):
    detalles = DetalleOrden.objects.all()
    return render(request, 'admin/detalle_orden_list.html', {'detalles': detalles})

# Agregar Detalle de Orden
@login_required
def detalle_orden_create(request):
    if request.method == 'POST':
        form = DetalleOrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_detalleorden_list')
    else:
        form = DetalleOrdenForm()
    return render(request, 'admin/detalle_orden_form.html', {'form': form})

# Editar Detalle de Orden
@login_required
def detalle_orden_edit(request, id_det):
    detalle = get_object_or_404(DetalleOrden, pk=id_det)
    if request.method == 'POST':
        form = DetalleOrdenForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('admin_detalleorden_list')
    else:
        form = DetalleOrdenForm(instance=detalle)
    return render(request, 'admin/detalle_orden_form.html', {'form': form})

# Eliminar Detalle de Orden
@login_required
def detalle_orden_delete(request, id_det):
    detalle = get_object_or_404(DetalleOrden, pk=id_det)
    if request.method == 'POST':
        detalle.delete()
        return redirect('admin_detalleorden_list')
    return render(request, 'admin/detalle_orden_confirm_delete.html', {'detalle': detalle})

from django.http import FileResponse
import os

@permission_required('app_db.view_producto', raise_exception=True)  # Cambia el permiso según sea necesario
def descargar_respaldo(request):
    db_file = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    backup_file = os.path.join(settings.BASE_DIR, 'backup.sqlite3')

    if os.path.exists(db_file):
        with open(db_file, 'rb') as db, open(backup_file, 'wb') as backup:
            backup.write(db.read())

        return FileResponse(open(backup_file, 'rb'), as_attachment=True, filename='backup.sqlite3')
    else:
        return HttpResponseNotFound('El archivo de la base de datos no existe.')

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
import os

@permission_required('app_db.add_producto', raise_exception=True)  # Cambia el permiso según sea necesario
def subir_respaldo(request):
    if request.method == "POST" and request.FILES.get("backup_file"):
        backup_file = request.FILES["backup_file"]
        backup_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')

        with open(backup_path, "wb") as db_file:
            for chunk in backup_file.chunks():
                db_file.write(chunk)

        return HttpResponse("Respaldo restaurado con éxito.")
    return render(request, 'admin/subir_respaldo.html')

# Dashboard
@login_required
def admin_dashboard(request):
    # Esta vista muestra un dashboard con enlaces a las secciones administrativas.
    return render(request, 'admin/dashboard.html')