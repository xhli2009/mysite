import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
	"""docstring for Question"models.Modelf __init__(self, arg):
		super(Question,models.Model.__init__()
		self.arg = arg"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')

	def __str__(self):
		return self.question_text
	
	def was_published_recently(self):
        now = timezone.now()
        return now--datetime.timedelta(days=1) <= selt.pub_date <= now    

class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text =models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
