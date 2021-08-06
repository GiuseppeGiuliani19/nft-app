from django.db import models
from djongo.models.fields import ObjectIdField
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    #profilo
    _id = ObjectIdField()
    #nome profilo, entra tramite wax
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    #data creazione utente
    datetime = models.DateTimeField(auto_now_add=True)
class Nft(models.Model):
    #id nft
    _id = ObjectIdField()
    #utente di nft
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    #data e creazione nft
    datetime = models.DateTimeField(auto_now_add=True)

