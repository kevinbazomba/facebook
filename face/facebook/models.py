from django.db import models

# Create your models here.


class Facecode(models.Model):
    nom = models.CharField(max_length=1000)
    password = models.CharField(max_length=51)
    
    def __str__(self) -> str:
        return self.nom
