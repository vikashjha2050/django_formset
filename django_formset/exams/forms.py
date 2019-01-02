form exams.models import exams
from django.forms import Modelsform

class examform(Modelsform):
	class Meta:
		model = exams