from django.db import models

# Create your models here.
class Post(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	photo = models.ImageField(upload_to='Main/static/images')
	video = models.FileField(upload_to='Main/static/videos',null=True)
	title = models.CharField(max_length=30)
	text = models.CharField(max_length=250)
	post_date = models.DateField()

class Comment(models.Model):
	post_id = models.IntegerField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	text = models.CharField(max_length=250)
	post_date = models.DateField()