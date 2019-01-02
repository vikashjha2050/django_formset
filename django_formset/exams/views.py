from django.shortcuts import render
from django.views.generic.list import ListView

from exams.models import exams
from exams.forms import ExamForm
# Create your views here.

class dashboard(ListView):
	model = exams
	template_name = 'exams/exam_dashboard.html'

def exam_add_edit(request):
	exform = ExamForm()
	if request.method == 'POST':
		exform = ExamForm(request.POST)
		if exform.is_valid():
			exform.save()
	return render(request, 'exams/exam_create.html',{'exform':exform})
