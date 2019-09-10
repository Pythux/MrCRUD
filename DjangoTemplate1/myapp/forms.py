
from django import forms
from .models import Post

# class FormName(forms.Form):
#     title = forms.CharField()
#     contente = forms.CharField(widget=forms.Textarea)


class FormName(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
