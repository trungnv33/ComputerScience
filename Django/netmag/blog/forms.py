from .models import Post
from django import forms
import datetime
class RawPostForm(forms.Form):
    title = forms.CharField(initial= 'Trung')
    slug = forms.SlugField()
    description =  forms.CharField()
    content = forms.CharField()
    published = forms.BooleanField(required=False)
    created = forms.DateTimeField(initial=datetime.date.today)
