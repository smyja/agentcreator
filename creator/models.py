from django.db import models

# Create your models here.

class Llm(models.Model):
    name=models.CharField(max_length=160, blank=True)
    
    def __str__(self):
        return self.name