from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.http import HttpResponse

from exams.models import exams, SubExam
from exams.forms import ExamForm, SubExamForm
# Create your views here.

class dashboard(ListView):
	model = exams
	template_name = 'exams/exam_dashboard.html'

def exam_add(request):
	exform = ExamForm()
	subexformset = modelformset_factory(SubExam, form=SubExamForm, extra = 1)
	subexformset = subexformset(request.POST or None, queryset = SubExam.objects.filter(id__isnull = True))
	if request.method == 'POST':
		exam = exams()
		exform = ExamForm(request.POST, instance = exam)
		if exform.is_valid() and subexformset.is_valid():
			exform.save()
			instances = subexformset.save(commit=False)
			for subexform in instances:
				subexform.parent_exam = exam.id
				subexform.save()
			return redirect('/exams/dashboard/')
		else:
			print('invalid data')

	return render(request, 'exams/exam_create.html',{'exform':exform,'exformset': subexformset})

def exam_edit(request, pk = None):
	exam = exams.objects.get(id = pk)
	print(exam)
	exform = ExamForm( instance = exam)
	subexformset = modelformset_factory(SubExam, form=SubExamForm, extra=1)
	subexformset = subexformset(request.POST or None, queryset = SubExam.objects.filter(parent_exam = pk))
	if request.method == 'POST':
		exform = ExamForm(request.POST, instance = exam)
		if exform.is_valid() and subexformset.is_valid():
			exform.save()
			instances = subexformset.save(commit=False)
			for subexform in instances:
				subexform.parent_exam = exam.id
				subexform.save()
			return redirect('/exams/dashboard/')
		else:
			print('invalid data')

	return render(request, 'exams/exam_create.html',{'exform':exform,'exformset': subexformset})

def getset(request):
	subexformset = modelformset_factory(SubExam, form=SubExamForm, extra = 1)
	subexformset = subexformset(request.POST or None, queryset = SubExam.objects.filter(id__isnull = True))

	return HttpResponse(subexformset)
