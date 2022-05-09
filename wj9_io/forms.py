from django import forms
from .models import DigitalProduct

class DigitalProductForm(forms.ModelForm):
    class Meta:
        model=DigitalProduct
        fields=['name','file']
        labels={'name':'Name', 'file':'File'}
        widgets={'name':forms.Textarea(attrs={'cols':2,'rows':2}),'file':forms.ClearableFileInput()}