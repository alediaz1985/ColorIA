# apps/analisis/forms.py

from django import forms

class ImagenForm(forms.Form):
    imagen = forms.ImageField(label='Subí una imagen', required=False)
