from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here
class Categorie (models.Model):
    name = models.CharField(max_length=100 , null = True)
    slug = models.CharField(max_length=100 , null = True) 
    def __str__(self):
        return str(self.id) + " _ "+ self.name


class Produit(models.Model):
    name = models.CharField(max_length=200 , null = True)
    prix = models.IntegerField(null = True )
    qte = models.IntegerField(null = True)
    
    categorie = models.ForeignKey(Categorie , on_delete= models.CASCADE , null = True)
    def __str__(self) -> str:
        return self.name

class Produit_Image(models.Model):
    produit = models.ForeignKey(Produit , on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'images' , null = True)
    def __str__(self):
        return self.produit.name+" is image"

class Picture(models.Model):
    image = models.ImageField(upload_to = 'images' , null = True)