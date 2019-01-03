from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.forms import modelformset_factory

from exams.models import exams, SubExam
from exams.forms import ExamForm, SubExamForm
# Create your views here.

class dashboard(ListView):
	model = exams
	template_name = 'exams/exam_dashboard.html'

def exam_add(request):
	exform = ExamForm()
	subexformset = modelformset_factory(SubExam, form=SubExamForm, extra = 2)
	subexformset = subexformset(request.POST or None, queryset = 	SubExam.objects.filter(id__isnull = True))
	if request.method == 'POST':
		exam = exams()
		exform = ExamForm(request.POST, instance = exam)
		if exform.is_valid() and subexformset.is_valid():
			exform.save()
			instances = subexformset.save(commit=False)
			for subexform in instances:
				print(exam.id)
				subexform.parent_exam = exam.id
				subexform.save()
			return redirect('/exams/dashboard/')
		else:
			print('invalid data')

	return render(request, 'exams/exam_create.html',{'exform':exform,'exformset': subexformset})

def exam_edit(request, pk=None):
	exform = ExamForm()
	if request.method == 'POST':
		exform = ExamForm(request.POST)
		if exform.is_valid():
			exform.save()
			return redirect('/exams/dashboard/')
	return render(request, 'exams/exam_create.html',{'exform':exform})
