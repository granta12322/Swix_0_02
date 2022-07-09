from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(default = "My Fun Event", max_length= 100)
    venue = models.ForeignKey(to = "Venue", related_name= "events", on_delete= models.CASCADE,null = True)
    creation_date = models.DateField(auto_now_add = True)
    start_datetime = models.DateTimeField(null = False, default = "2022-12-07 12:00:00")

class Venue(models.Model):
    name = models.CharField(default = "My House", max_length= 100)
    address = models.CharField(default = "9 Bruce Street", max_length= 100)


