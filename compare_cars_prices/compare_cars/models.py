import datetime
from django.db import models
from django.utils import timezone



class CarDetails(models.Model):
	website_name = models.CharField(max_length=100,blank=True)
	city = models.CharField(max_length=100,blank=True)
	makes = models.CharField(max_length=100,blank=True)
	car_model =models.CharField(max_length=100,blank=True)
	price = models.CharField(blank=True)
	model_year = models.CharField(blank=True)
	car_title = models.CharField(max_length=500,blank=True)
	car_href = models.URLField(max_length=5000,blank=True)
	car_image = models.ImageField(max_length=500,blank=True)
	car_color = models.CharField(max_length=50,blank=True)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.website_name


class CarMakeDetails(models.Model):
	website_name = models.CharField(max_length=100,blank=True)
	city = models.CharField(max_length=100,blank=True)
	makes = models.CharField(max_length=100,blank=True)
	car_model =models.CharField(max_length=100,blank=True)
	price = models.CharField(max_length=100,blank=True)
	model_year = models.CharField(max_length=100,blank=True)
	car_title = models.CharField(max_length=500,blank=True)
	car_href = models.URLField(max_length=5000,blank=True)
	car_image = models.ImageField(max_length=500,blank=True)
	car_color = models.CharField(max_length=50,blank=True)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.website_name



	def __str__(self):
		return self.car_model
# Create your models here.
