from unicodedata import name
from django.urls.conf import path
from csit.views import SemesterDetailView, SemesterView, SubjectDetailView

urlpatterns = [
	path('', SemesterView.as_view(), name = "csit"),
	path('<int:pk>/', SemesterDetailView.as_view(), name='semester-detail'),
	path('<slug:slug>/', SubjectDetailView.as_view(), name='subject-detail')
	
]

