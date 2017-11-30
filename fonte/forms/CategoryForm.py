from django import forms
from fonte.models import Font, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Nome:")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)