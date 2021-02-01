from django.contrib import admin
from .models import Domaine, Cours, CatQuestion, Question,Etudiant,Session_cours
#Register your models here.
admin.site.register(Domaine)
admin.site.register(Cours)
admin.site.register(Etudiant)
admin.site.register(CatQuestion)
admin.site.register(Question)
admin.site.register(Session_cours)

