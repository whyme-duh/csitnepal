from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic import ListView

from csit.models import NoteFile, Semester, Subject


# it shows the list of the semester
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
        


# it shows the list of the files on the respective subjects

class SubjectDetailView(ListView):
    model = NoteFile
    template_name = 'csit/notefiles_detail.html'
    context_object_name = "notes"

    def get_queryset(self):
        slug = get_object_or_404(Subject, slug =self.kwargs.get('slug'))
        return NoteFile.objects.filter(subject = slug)
    
  

    
