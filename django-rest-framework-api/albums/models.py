# Django
from django.db import models

''' Create a model class Album '''
class Album(models.Model):
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
      
''' Create a model class Record '''
class Record(models.Model):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    record_number = models.PositiveIntegerField(blank=True, null=True)
    slug = models.SlugField()

    
    class Meta:
        ordering = ['album', 'record_number']
    
    def __str__(self):
        return self.name
    
    
