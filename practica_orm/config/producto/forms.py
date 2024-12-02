from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'fecha_vencimiento']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto', 
            'descripcion': 'Descripción del producto',
            'fabrica': 'Fábrica',
            'fecha_vencimiento': 'Fecha de vencimiento'
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'fabrica': forms.Select(attrs={'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(attrs={
                'class':'form-control',
                'type':'date',
                'placeholder':'dd/mm/aaaa'
            })
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_vencimiento'].input_formats = ['%d/%m/%Y']
        
        
        
