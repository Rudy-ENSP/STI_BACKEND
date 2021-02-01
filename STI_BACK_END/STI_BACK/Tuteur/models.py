from django.db import models
from django.contrib.auth.models import User
from STI_BACK.settings import BASE_DIR

# Create your models here.
class Domaine(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
    	return str(self.name)

class Cours(models.Model):
    id = models.AutoField(primary_key=True)
    domaine=models.ManyToManyField(Domaine)
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    contenu=models.CharField(max_length=10000)
    ressource=models.FileField(upload_to='Ressources')
    def __str__(self):
    	return str(self.name)

class Etudiant(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    connaissance= models.ManyToManyField(Domaine)
    cours=models.ManyToManyField(Cours)
    name=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email=models.EmailField(max_length=256,default=None)
    niveau_social=models.CharField(max_length=50)
    sexe=models.CharField(max_length=50)
    age=models.IntegerField()
    def __str__(self):
    	return str(self.user.username)+" "+str(self.user.id)

class Session_cours(models.Model):
    id = models.AutoField(primary_key=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours=models.ForeignKey(Cours, on_delete=models.CASCADE)
    progression=models.IntegerField()
    note=models.IntegerField()
    pourcentage_erreur_section1=models.IntegerField(default=33)
    pourcentage_erreur_section2=models.IntegerField(default=33)
    pourcentage_erreur_section3=models.IntegerField(default=34)
    def __str__(self):
    	return str(self.cours.name) 


class CatQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self):
    	return str(self.name) 

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    domaine=models.ForeignKey(Domaine, on_delete=models.CASCADE)
    categorie=models.ForeignKey(CatQuestion, on_delete=models.CASCADE)
    cours=models.ForeignKey(Cours,on_delete=models.CASCADE)
    libellé = models.CharField(max_length=50)
    reponse=models.CharField(max_length=50)
    libellé_reponse=models.CharField(max_length=200)
    section=models.IntegerField(default=None)
    def __str__(self):
    	return str(self.libellé)  

