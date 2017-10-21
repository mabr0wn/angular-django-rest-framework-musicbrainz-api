from django.db import models.

''' Create a model class Collection '''
class Collection(models.Model):
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
    collection = models.ForeignKey(Collection)
    record_number = models.PostiveIntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ['collection', 'record_number']
    
    def __str__(self):
        return self.name
    
    
