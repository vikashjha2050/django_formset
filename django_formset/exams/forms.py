from django.forms import ModelForm
from exams.models import exams

class ExamForm(ModelForm):
	class Meta:
		model = exams
		fields = '__all__'