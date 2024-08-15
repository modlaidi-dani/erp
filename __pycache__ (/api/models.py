from django.db import models

# Create your models here.
class SinfInd(models.Model):
    sinf=models.CharField(max_length=100, null=True)
    numind=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.sinf}"
class Degret(models.Model):
    degret=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.degret}"

class Table(models.Model):
    sinf=models.ForeignKey(SinfInd,null=True, on_delete=models.CASCADE)
    degret=models.ForeignKey(Degret, on_delete=models.CASCADE)
    val=models.IntegerField()

class   Administration(models.Model):
    name=models.CharField(max_length=200)
    valeur=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.name}"
class Section(models.Model):
    name=models.CharField(max_length=200)
    administration=models.ManyToManyField(Administration)
    def __str__(self) -> str:
        return f"{self.name}"

class Postedispo(models.Model):
    nameposte=models.CharField(max_length=200)
    sinf=models.ForeignKey(SinfInd,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.nameposte}"
class Poste(models.Model):
    poste=models.ForeignKey(Postedispo,on_delete=models.CASCADE,null=True)
    administration= models.ForeignKey(Administration, on_delete=models.CASCADE,null=True)
    section= models.ForeignKey(Section,on_delete=models.CASCADE,null=True)
    degret=models.ForeignKey(Degret,on_delete=models.CASCADE,null=True)
    slairebase= models.IntegerField()
    primeAdministration=models.IntegerField(default=0)
    primeAutre=models.IntegerField(default=0)
    salairefinale=models.IntegerField(default=0)
