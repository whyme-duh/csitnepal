from unicodedata import name
from django.urls.conf import path
from csit.views import  semesterView, SubjectDetailView, NoteFileDetailView, semesterDetailView

urlpatterns = [
	path('', semesterView, name = "csit"),
	path('semester/<int:semester_slug>/', semesterDetailView, name='semester-detail'),
	path('semester/<int:semester_slug>/<slug:subject_name>/', SubjectDetailView, name='subject-detail'),
	path('semester/<int:semester_slug>/<slug:subject_name>/<slug:filename>/', NoteFileDetailView, name='single-file-detail'),
	
]

