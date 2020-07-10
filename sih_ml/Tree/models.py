from django.db import models
from django.db.models import Model, CharField, ForeignKey, BooleanField

class Tree(Model):
    name = CharField(max_length=30)
    parent = ForeignKey("self", null=True, blank=True,on_delete=models.CASCADE)
    Level=models.SmallIntegerField()
    def __str__(self):
        return self.name