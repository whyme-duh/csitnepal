from unicodedata import name
from django.urls.conf import path
from csit.views import  SemesterView, SubjectDetailView, NoteFileDetailView, semesterDetailView

urlpatterns = [
	path('', SemesterView.as_view(), name = "csit"),
	path('semester/<int:semester_slug>/', semesterDetailView, name='semester-detail'),
	path('semester/<int:semester_slug>/<slug:subject_name>/', SubjectDetailView, name='subject-detail'),
	path('semester/<int:semester_slug>/<slug:subject_name>/<slug:filename>/', NoteFileDetailView, name='single-file-detail'),
	
]

