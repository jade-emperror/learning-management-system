from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('syllabusfeed/',SyllabusFeed,name='syllabusfeed'),
    path('subjectfeed/',SubjectFeed,name='syllabusfeed'),
    path('logout/',clearses,name='syllabusfeed'),
    path('search/',search,name='syllabusfeed'),
    path('profile/',profile,name='syllabusfeed'),
]