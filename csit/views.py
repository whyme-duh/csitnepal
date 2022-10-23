from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic import ListView
from django.template import RequestContext

from csit.models import NoteFile, Semester, Subject




def error_404_view(request, exception):
    return render(request, '404.html')

def error_500_view(request):
    return render(request, 'csit/404.html')
# it shows the list of the semester

def counting(request):
    notescount = NoteFile.objects.filter(category = 1).count()
    return render(request, 'csit/notefiles_detail.html', {'notescount' : notescount})





class SemesterView(ListView):   
    # this views gives the list of all the semesters 
    model = Semester
    template_name = 'csit/csit.html'
    context_object_name = "semester"

def semesterView(request):
    if 'subjects' in request.GET:
        result = request.GET['subjects']
        semester = Subject.objects.filter(title__icontains = result)
        file = 'csit/search_result.html'
    else:
        semester = Semester.objects.all()
        file = 'csit/csit.html'
    context= {
        'semester': semester
    }
    return render(request, file,context )

# it shows the list of the subjects on the respective semester
    # class SemesterDetailView(ListView):
    #     model = Subject
    #     template_name = 'csit/subjects_detail.html'
    #     context_object_name = "subjects"
        
    #     # here , only the objects related to pk of the semester are passed
    #     # it filter the Subjects where the semester is eqaul to the pk of the semester
    #     def get_queryset(self):
    #         id = get_object_or_404(Semester, pk =self.kwargs.get('pk'))
    #         return Subject.objects.filter(semester = id)
        

def semesterDetailView(request, semester_slug):
    id = get_object_or_404(Semester, pk = semester_slug)
    subjects = Subject.objects.filter(semester = id)
    semesters = Semester.objects.filter().exclude(title = id)
    return render(request, 'csit/subjects_detail.html' , {"subjects" : subjects, 'semester' : semesters})


# it shows the list of the files on the respective subjects


def SubjectDetailView(request, semester_slug, subject_name):
    slug = get_object_or_404(Subject, semester= semester_slug, slug = subject_name)
    notes =  NoteFile.objects.filter(subject = slug)
    return render(request, 'csit/notefiles_detail.html', {
        "notes": notes,
        "subjects" : Subject.objects.filter(semester = semester_slug).exclude(title = slug)
    } )
# class SubjectDetailView(ListView):
#     model = NoteFile
#     template_name = 'csit/notefiles_detail.html'
#     context_object_name = "notes"

#     def get_queryset(self):

#         slug = get_object_or_404(Subject, slug =self.kwargs.get('slug'))
#         return NoteFile.objects.filter(subject = slug)
    


def NoteFileDetailView(request,semester_slug, subject_name,  filename):
    # this will retrieve an Subject object with requested semester and subjects
    slug = get_object_or_404(Subject, semester= semester_slug, slug = subject_name)
    fname = get_object_or_404(NoteFile, slug = filename )
    return render(request, 'csit/SingleNoteFile.html', {
        "notes" : NoteFile.objects.filter(slug = filename),
        "related_notes" : NoteFile.objects.filter(subject = slug).exclude(slug = filename),
    })




