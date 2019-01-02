from django.shortcuts import render
from exams.forms import ExamForm
# Create your views here.

def exam_add_edit(request):
	exform = ExamForm()
	if request.method == 'POST':
		exform = examform(request.POST)
		exform.save()
	render(exform, 'exams/exam_create.html')
