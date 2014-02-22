from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import Blog

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Blog

    def save(self, commit=True):
        instance = super(BlogForm, self).save(commit=False)
        instance.published = True 
        if commit:
            instance.save()
        return instance

