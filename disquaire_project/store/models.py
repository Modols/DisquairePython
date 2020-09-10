# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField('Nom', max_length=200, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "artiste"

class Contact(models.Model):
    email = models.EmailField('Email',max_length=100)
    name = models.CharField('Nom',max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "contact"

class Album(models.Model):
    reference = models.IntegerField('Réference',null=True)
    created_at = models.DateTimeField('Crée à',auto_now_add=True)
    available = models.BooleanField('Disponible',default=True)
    title = models.CharField('Titre',max_length=200)
    picture = models.URLField("Pochette d'album",)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "album"

class Booking(models.Model):
    created_at = models.DateTimeField('Crée à',auto_now_add=True)
    contacted = models.BooleanField('Demande traité ?',default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album)
    def __str__(self):
        return self.contact.name
    class Meta:
        verbose_name = "booking"