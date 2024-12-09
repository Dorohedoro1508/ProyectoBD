from django import forms
from app_db.models import Producto, Inventario, Empleado, Distribuidor, OrdenDistribuidor, DetalleOrden  # type: ignore
from django.shortcuts import render, get_object_or_404, redirect


class DistribuidorForm(forms.ModelForm):
    class Meta:
        model = Distribuidor
        fields = ['nom_dis', 'tel_dis', 'dir_dis']
        widgets = {
            'nom_dis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del distribuidor'}),
            'tel_dis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'dir_dis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        }
        error_messages = {
            'nom_dis': {
                'required': 'El nombre del distribuidor es obligatorio.',
                'max_length': 'El nombre no puede tener más de 50 caracteres.',
            },
            'tel_dis': {
                'invalid': 'Por favor, introduce un número de teléfono válido.',
            },
        }

    # Validación personalizada
    def clean_tel_dis(self):
        tel_dis = self.cleaned_data.get('tel_dis')
        if tel_dis and len(str(tel_dis)) != 10:
            raise forms.ValidationError('El número de teléfono debe tener exactamente 10 dígitos.')
        return tel_dis

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nom_pro', 'des_pro', 'pre_pro']
        widgets = {
            'nom_pro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'des_pro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'pre_pro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
        }
        error_messages = {
            'nom_pro': {'required': 'El nombre del producto es obligatorio.'},
            'pre_pro': {'invalid': 'El precio debe ser un número válido.'},
        }

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['fec_inv', 'can_inv', 'ubi_inv', 'id_pro']
        widgets = {
            'fec_inv': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'can_inv': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'ubi_inv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'id_pro': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'can_inv': {'invalid': 'Por favor, introduce una cantidad válida.'},
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nomb_emp', 'pue_emp', 'fec_emp']
        widgets = {
            'nomb_emp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'pue_emp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Puesto'}),
            'fec_emp': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class DistribuidorForm(forms.ModelForm):
    class Meta:
        model = Distribuidor
        fields = ['nom_dis', 'tel_dis', 'dir_dis']
        widgets = {
            'nom_dis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del distribuidor'}),
            'tel_dis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'dir_dis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        }

class OrdenDistribuidorForm(forms.ModelForm):
    class Meta:
        model = OrdenDistribuidor
        fields = ['fec_ord', 'est_ord', 'id_dis', 'id_emp']
        widgets = {
            'fec_ord': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'est_ord': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'id_dis': forms.Select(attrs={'class': 'form-control'}),
            'id_emp': forms.Select(attrs={'class': 'form-control'}),
        }

def orden_distribuidor_form(request, id_ord=None):
    # Obtener datos necesarios para las listas desplegables
    distribuidores = Distribuidor.objects.all()
    empleados = Empleado.objects.all()

    if id_ord:
        orden = get_object_or_404(OrdenDistribuidor, id_ord=id_ord)
    else:
        orden = None

    if request.method == "POST":
        fec_ord = request.POST.get("fec_ord")
        est_ord = request.POST.get("est_ord")
        id_dis = request.POST.get("id_dis")
        id_emp = request.POST.get("id_emp")

        distribuidor = get_object_or_404(Distribuidor, id_dis=id_dis)
        empleado = get_object_or_404(Empleado, id_emp=id_emp)

        if orden:
            orden.fec_ord = fec_ord
            orden.est_ord = est_ord
            orden.id_dis = distribuidor
            orden.id_emp = empleado
            orden.save()
        else:
            OrdenDistribuidor.objects.create(
                fec_ord=fec_ord, est_ord=est_ord, id_dis=distribuidor, id_emp=empleado
            )
        return redirect("admin_ordendistribuidor_list")

    return render(request, "orden_distribuidor_form.html", {
        "orden": orden,
        "distribuidores": distribuidores,
        "empleados": empleados,
    })

class DetalleOrdenForm(forms.ModelForm):
    class Meta:
        model = DetalleOrden
        fields = ['id_ord', 'id_pro', 'can_pro', 'pre_uni']
        widgets = {
            'id_ord': forms.Select(attrs={'class': 'form-control'}),
            'id_pro': forms.Select(attrs={'class': 'form-control'}),
            'can_pro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'pre_uni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio Unitario'}),
        }
