from django.shortcuts import render
from exams.forms import ExamForm
# Create your views here.

def exam_add_edit(request):
	exform = ExamForm()
	print(request.method)
	if request.method == 'POST':
		exform = ExamForm(request.POST)
		if exform.is_valid():
			exform.save()
	return render(request, 'exams/exam_create.html',{'exform':exform})
