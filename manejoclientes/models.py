from django.db import models
from django.utils import timezone

class Client(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length= 100)
	card_id = models.CharField(max_length= 100)
	added_date = models.DateTimeField(default=timezone.now)
	active = models.BooleanField(default=True)

	def addUser(self):
		self.save()

	def __str__(self):
		return self.card_id