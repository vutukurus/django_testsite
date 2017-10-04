from django.db import models

# Create your models here.
#charflies -> text data
#integ --> integers
#slugfiled --> python_perl
#text field --> multople line
#date fled --> dates

#userand pwd table
class uname_pwd(models.Model):
	username = models.CharField(max_length=10)
	pwd = models.CharField(max_length=10)



class student(models.Model):
	name = models.TextField()
	age = models.IntegerField()

class vendor(models.Model):
	
	STATUS_CHOICES=(
	("paid", "PAID"),
	("unpaid","UNPAID"),
	)
	
	title = models.CharField(max_length=20)
	body = models.TextField()
	amount = models.IntegerField()
	status = models.CharField(max_length=20, choices = STATUS_CHOICES,default="unpaid")
	
	def __str__(self):
		return self.title