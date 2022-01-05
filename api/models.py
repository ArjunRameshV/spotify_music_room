import string
import random

from django.db import models

def  generate_unique_code():
    length = 6
    # generate a unique room codename
    while True:
        codename = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(codename=codename).count() == 0:
            break

    return codename


# Create your models here.
class Room(models.Model):
    codename = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=30, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_datetime = models.DateTimeField(auto_now_add=True)