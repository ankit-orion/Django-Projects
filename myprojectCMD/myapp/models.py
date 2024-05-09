from django.db import models

# Create your models here.
from django.db import models

class Emp(models.Model):
    
    
    # Define your Emp model fields here
    name=models.CharField(max_length=20)
class Emp(models.Model):
    
    # Model fields definition
    class Meta:
        
        app_label = 'myapp'  # Replace 'your_app_label' with the actual app label
