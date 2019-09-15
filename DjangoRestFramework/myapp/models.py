from django.db import models

# Create your models here.


class NicePlace(models.Model):
    place = models.CharField(max_length=50)
    coord_x = models.IntegerField()
    coord_y = models.IntegerField()

    def __str__(self):
        return "{}: {} - {}".format(self.place, self.coord_x, self.coord_y)
