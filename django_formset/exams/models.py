from django.db import models

# Create your models here.

class exams(models.Model):
	name = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name		

class SubExam(models.Model):
	parent_exam = models.IntegerField(default = None)
	name = models.CharField(max_length = 10, default=None, null=True, blank =True)
	institute = models.CharField(max_length = 20, default=None, null=True, blank =True)

	def __str__(self):
		return self.name