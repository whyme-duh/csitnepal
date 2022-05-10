from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic import ListView
from django.template import RequestContext

from csit.models import NoteFile, Semester, Subject


context = {
    'subjects' : Subject.objects.all(),
    'notes' : NoteFile.objects.all(),
    'semester': Semester.objects.all()
}

def error_404_view(request, exception):
    return render(request, '404.html')

def error_500_view(request):
    return render(request, 'csit/404.html')
# it shows the list of the semester

def counting(request):
    notescount = NoteFile.objects.filter(category = 1).count()
    return render(request, 'csit/notefiles_detail.html', {'notescount' : notescount})

class SemesterView(ListView):   
    model = Semester
    template_name = 'csit/csit.html'
    context_object_name = "semester"


# it shows the list of the subjects on the respective semester
class SemesterDetailView(ListView):
    model = Subject
    template_name = 'csit/subjects_detail.html'
    context_object_name = "subjects"
    
    # here , only the objects related to pk of the semester are passed
    # it filter the Subjects where the semester is eqaul to the pk of the semester
    def get_queryset(self):
        id = get_object_or_404(Semester, pk =self.kwargs.get('pk'))
        return Subject.objects.filter(semester = id)
        

def semesterDetailView(request):
    return render(request, 'csit/subjects_detail.html' , context)


# it shows the list of the files on the respective subjects

class SubjectDetailView(ListView):
    model = NoteFile
    template_name = 'csit/notefiles_detail.html'
    context_object_name = "notes"

    def get_queryset(self):
        slug = get_object_or_404(Subject, slug =self.kwargs.get('slug'))
        return NoteFile.objects.filter(subject = slug)
    
  

    
