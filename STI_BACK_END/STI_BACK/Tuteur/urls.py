
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Tuteur import views


urlpatterns = [
    #path('logout/', views.logout, name="logout"),
    path('login/', views.loginUser, name="login"),
    path('signup/', views.Signup, name='Signup'),
    path('completecourse/', views.TerminerCours, name='TerminerCours'),
    path('create_session/', views.create_session, name='create_session'),
    path('upgrade_progression/', views.upgrade_progression, name='upgrade_progression'),
    path('get_questions/', views.Envoyer_questions, name='Envoyer_questions'),
    path('listeDomaines/', views.listeDomaines, name='listeDomaines'),
    path('initialize_connaissance/', views.initialize_connaissance, name='initialize_connaissance'),
    path('Association_Rule_Mining/', views.Association_Rule_Mining, name='Association_Rule_Mining'),
    path('Evaluation/', views.Evaluation, name='Evaluation'),
    path('Recommandation1/', views.Recommandation1, name='Recommandation1')
    
]


