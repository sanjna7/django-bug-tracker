from django.db import models

class Bug(models.Model):
	title=models.CharField(max_length=100)
	discription=models.TextField()
	status=models.CharField(max_length=20, default='Open')
	created_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title
