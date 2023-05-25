from django import forms

from cargo.models import Cargo


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #
        #     for name, field in self.fields.items():
        #         field.widgets.attrs['class'] = 'form-control'
