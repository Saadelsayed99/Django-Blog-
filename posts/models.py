from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
# Create your models here.

'''
    -title
    -author
    -cotent
    -image
    -uplish_date
    -tags
'''

'''
    -fields
    -htmlwidget
    -validation
'''

class post(models.Model):
    auther =models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=50000)
    publish_date = models.DateTimeField()
    tags = TaggableManager()
    image = models.ImageField(upload_to='posts')
    
    def __str__(self):
        return self.title
    