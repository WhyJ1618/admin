from django.db import models

# Create your models here.
class Post(models.Model):
    #myname = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #mydate = models.DateTimeField('data published')
    def __str__(self):
        return self.title

