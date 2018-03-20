from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class attractionCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views= models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(attractionCategory, self).save(*args, **kwargs)
    
    
    class Meta:
        verbose_name_plural = 'attraction Categories'

    def __str__(self):
        return self.name


class attractionPage(models.Model):
    category = models.ForeignKey(attractionCategory,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
 

    def __str__(self):
        return self.title



                             
                             

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
