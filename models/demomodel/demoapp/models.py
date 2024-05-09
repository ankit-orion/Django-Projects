from django.db import models

# Create your models here.
class Blogpost(models.Model):
    
    post_id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=500, default="")
    thumbnail = models.ImageField(upload_to='images/', default="")
def __str__(self):
    return self.title
