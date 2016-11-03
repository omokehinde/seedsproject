from django.db import models


class NameNEmail(models.Model):
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.name + ', ' + self.email
