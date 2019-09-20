from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.name, self.niceplace_set)


class NicePlace(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                # related_name='niceplace_set'  # default name for list
                                )

    def __str__(self):
        return "{}: {} - {}".format(self.name, self.coord_x, self.coord_y)
