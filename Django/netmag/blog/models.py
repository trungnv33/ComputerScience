from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True, max_length= 255)
    description =  models.CharField(max_length= 255)
    content = models.TextField()
    published = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail',kwargs={'post_id':self.id})
    def get_home_url(self):
        return reverse('home')
class Document(models.Model):
    name=  models.CharField(max_length = 255)
    doc_file = models.FileField(upload_to='documents')