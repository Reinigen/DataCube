from django.db import models
from django.utils import timezone

# Create your models here.
class Algorithm(models.Model):
    Alg_Name =  models.CharField(max_length=300)
    Alg_Type =  models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.Alg_Name +", "+ self.Alg_Type

class Input(models.Model):
    Alg_solution =  models.CharField(max_length=300)
    Alg_problem = models.ForeignKey(Algorithm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + ": " + self.Alg_solution