from django.db import models
from users.models import User
from flights.models import Flight
# Create your models here.

class ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)