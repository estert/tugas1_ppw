from django import forms

class Message_Form(forms.Form):
    error_messages = {
        'required': 'Field ini wajib diisi',
		'invalid': 'Mohon diisi dengan link',
    }
    attrs = {
        'class': 'form-control'
    }

    name = forms.CharField(label='Nama', required=True, max_length=27,widget=forms.TextInput(attrs=attrs))
    url = forms.CharField(label='Heroku URL',widget=forms.URLInput(attrs=attrs), required=True)