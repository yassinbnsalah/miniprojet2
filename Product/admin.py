from django.contrib import admin
from .models import Categorie, Produit ,Produit_Image , Picture
# Register your models here.
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Picture)
admin.site.register(Produit_Image)