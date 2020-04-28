from django import forms

class UploadPicture(forms.Form):
    
    image = forms.FileField(label="Choose file!")