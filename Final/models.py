from django.db import models

# Create your models here.
class Imagen(models.Model):
    
    cadena = models.CharField(max_length=10000,default="", editable=False)
    cadena1 = models.IntegerField(default=0, editable=False)    
    #cadena=models.ImageField(upload_to= "Imagens")


    def __str__(self):
        print(self.cadena)
        return f"cadena: {self.cadena}"

    def newImagen(self,data,data2):
        #self.contador=data2
        self.cadena=data
        self.cadena1=data2