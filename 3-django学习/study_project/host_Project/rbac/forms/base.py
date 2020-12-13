from django import forms


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
