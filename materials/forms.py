from django import forms

from . import models


class MaterialModelForm(forms.ModelForm):
    class Meta:
        model = models.Material
        fields = '__all__'
