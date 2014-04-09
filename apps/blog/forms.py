#! coding=utf-8
import datetime

from django import forms
from django.template.defaultfilters import slugify

from pagedown.widgets import AdminPagedownWidget
from models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(label=u'标题', widget=forms.TextInput(attrs={'size':118}))
    content = forms.CharField(label=u'内容', widget=AdminPagedownWidget())
    #表单中不再使用sippet
    #snippet = forms.CharField(label=u'摘要', 
    #                            widget=forms.Textarea(attrs={'cols':85, 'rows':7}),
    #                            required=False
    #                         )
    class Meta:
        model = Blog
        # widgets = {
        #     'snippet': forms.Textarea(attrs={'rows':4,'cols':15}),
        # }

    def save(self, commit=True):
        instance = super(BlogForm, self).save(commit=False)
        if instance.status == 'p' and instance.publish_time is None:
            instance.publish_time = datetime.datetime.now()  
        if commit:
            instance.save()
        return instance

