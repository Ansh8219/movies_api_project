from django.db import models 

# Create your models here.
class WatchList(models.Model):
    title=models.CharField( max_length=50)
    storyline =models.CharField(max_length = 300)
    platform=models.ForeignKey('StreamPlatform' ,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class StreamPlatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField( max_length=50)
    website=models.URLField(max_length=200)
     
    def __str__(self):
        return self.name


    