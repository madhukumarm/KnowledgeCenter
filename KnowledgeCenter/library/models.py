from django.db import models

PAYMENT_CHOICES = [
		('free', 'Free'),
		('paid', 'Paid'),
]
# Create your models here.
class BookModel(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100,blank=True)
	genre = models.CharField(max_length=100)
	in_stock = models.BooleanField(default=True)
	free_or_paid = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='free')

	class Meta:
		verbose_name = 'Book'
		verbose_name_plural = 'Books'

	def __str__(self):	#class based method
		return self.title
