from django.db import models

# Create your models here.


class NicePlace(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()

    def __str__(self):
        return "{}: {} - {}".format(self.name, self.coord_x, self.coord_y)


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    niceplace = models.OneToOneField(NicePlace, on_delete=models.CASCADE,
                                     # related_name='niceplace_set'  # default name for list
                                     )

    def __str__(self):
        return "{}: {}".format(self.name, self.niceplace)
