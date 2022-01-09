from django.test import TestCase

# Create your tests here.
import datetime

from thehood.forms import NeighbourHoodForm
from .views import profile
from .models import Business, NeighbourHood, Post, Profile 
from django.contrib.auth.models import User
from django.test import TestCase

class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="username", password="password")
        self.user.save()
        self.profile = Profile(email='aa@gmail.com', photo='', bio='xxxx',
                                    user=self.user)
        self.profile.save()
        self.neighbourhood =  NeighbourHood(name = "Nairobi", location= "Ngara", admin = self.profile,description='xxxx', photo="")
        self.neighbourhood.save()
        
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)


class NeighbourHoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="tary", password="123")
        self.user.save()
        self.neighbourhood =  NeighbourHood(name = "Nairobi", location= "Ngara", admin = self.user,description='xxxx', photo="")
        self.neighbourhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,NeighbourHood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_neighbourhood()
        neighbourhood = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_neighbourhoodhood(self):
        self.neighbourhood.delete_neighbourhood()
        testsaved = NeighbourHood.objects.all()
        self.assertFalse(len(testsaved) > 0)


class BusinessTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="tary", password="123")
        self.user.save()
        self.neighbourhood =  NeighbourHoodForm(name = "Nairobi", location= "Ngara", admin = self.user,description='tarararra')
        self.neighbourhood.save()
        self.business = Business(user=self.user,name="asap", neighbourhood=self.neighbourhood,email="aa@gmail.com", description="xxxx")
        self.business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_save_business(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_business(self):
        self.business.delete_business()
        business = Business.objects.all()
        self.assertFalse(len(business) > 0)