from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, default='')
    image = CloudinaryField('profile-photo', null=True, transformation=[{'width':300, 'height':300}])
    bio = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    photo = CloudinaryField('image')
    description = models.TextField()
    occupants_count= models.IntegerField( default=0, blank=True)
    health_toll =  models.IntegerField(null=True, blank=True)
    police_toll =  models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()
class Post(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=255)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='posting')
    user = user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='developer')