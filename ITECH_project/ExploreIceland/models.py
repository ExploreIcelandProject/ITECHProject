from django.db import models



class attractionCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'attraction Categories'

    def __str__(self):
        return self.name


class attractionPage(models.Model):
    category = models.ForeignKey(attractionCategory)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
