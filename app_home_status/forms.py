from django import forms

class Status_Form(forms.Form):
    status_attrs = {
        'type': 'text',
        'rows': 4,
        'class' : 'form-control',
        'placeholder':"What's happening?",
        'style' : 'resize:none'
    }

    status = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=status_attrs))

class Comment_Form(forms.Form):
    comment_attrs = {
        'type': 'text',
        'rows': 4,
        'class' : 'form-control',
        'placeholder':"Ketik your comment here..",
        'style' : 'resize:none'
    }

    nama_attrs = {
        'type': 'text',
        'rows': 1,
        'class' : 'form-control',
        'placeholder':"Ketik nama lu..",
        'style' : 'resize:none'
    }
    
    nama = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=nama_attrs))
    comment = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=comment_attrs))
    