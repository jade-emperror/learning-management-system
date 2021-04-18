from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('syllabusfeed/',SyllabusFeed,name='syllabusfeed'),
    path('subjectfeed/',SubjectFeed,name='syllabusfeed'),
    path('clearses/',clearses,name='syllabusfeed'),
]