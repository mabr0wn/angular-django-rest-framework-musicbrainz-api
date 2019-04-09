# Django
from django.db import models

''' Create a model class Assortment '''
class Assortment(models.Model):
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
    assortment = models.ForeignKey(Assortment, on_delete=models.CASCADE)
    record_number = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ['assortment', 'record_number']
    
    def __str__(self):
        return self.name
    
    
