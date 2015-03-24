from django.db import models


class Question(models.Model):
    texte = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.texte


class Reponse(models.Model):
    question = models.ForeignKey('Question')
    texte = models.CharField(max_length=100)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.texte
