from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=150)
	author = models.ManyToManyField("Author", related_name="books")
	review = models.TextField(blank=True, null=True)
	date_reviewed = models.DateTimeField(blank=True, null=True)
	is_favorite = models.BooleanField(default=False, verbose_name="Favorite?")

	def __str__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=70, help_text="Use pen name, not realname",
							unique=True)
	def __str__(self):
		return self.name
