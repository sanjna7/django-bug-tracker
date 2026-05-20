from django.db import models

class Bug(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField(blank=True, null=True)
	status=models.CharField(max_length=20, default='open')
	created_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	
