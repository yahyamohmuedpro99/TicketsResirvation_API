from django.db import models

# think about it like simple reservation sys okay we have like 3 states
# to have on each use 
# Guest ----reserve---- movie so here is our 3 tables we need to have

class Movie(models.Model):
    hall=models.CharField(max_length=10)
    movie=models.CharField(max_length=10)
    date=models.DateField(max_length=10)

class Guest(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=12)

class Reservation(models.Model):
    # related name is important bcz it let you query on cross models 
    # allows you to access all reservations for a (guest,movie)
    guest=models.ForeignKey(Guest,related_name='resrvation',on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,related_name='resrvation',on_delete=models.CASCADE)