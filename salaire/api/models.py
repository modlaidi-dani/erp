from django.db import models

# Create your models here.
class SinfInd(models.Model):
    sinf=models.IntegerField()
    numind=models.IntegerField()
class ValerInd(models.Model):
    deg=models.IntegerField()
    sinf=models.ForeignKey(SinfInd, on_delete=models.CASCADE)
    val=models.IntegerField()
class   Administration(models.Model):
    name=models.CharField(max_length=200)
    valeur=models.IntegerField()

class Section(models.Model):
    name=models.CharField(max_length=200)
    administration=models.ManyToManyField(Administration)

class Poste(models.Model):
    name=models.CharField(max_length=200)
    administration= models.ForeignKey(Administration, on_delete=models.CASCADE)
    section= models.ForeignKey(Section,on_delete=models.CASCADE)
    sinf=models.ForeignKey(SinfInd,on_delete=models.CASCADE)
    valeuridentifiant=models.ForeignKey(ValerInd,on_delete=models.CASCADE)
    slairebase= models.IntegerField()
    primeAdministration=models.IntegerField(default=00)
    primeAutre=models.IntegerField(default=00)
    salairefinale=models.IntegerField(default=00)
