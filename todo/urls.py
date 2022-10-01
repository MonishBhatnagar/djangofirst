from django.conf.urls import url
from todo.views import contact,about,todolist,todoadd,service,home,todoedit,tododelete
urlpatterns=[
    url(r'^$',todolist,name='todolist'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^add/$',todoadd,name='todoadd'),
    url(r'^service/$',service,name='service'),
    url(r'^about/$',about,name='about'),
    url(r'^edit/(?P<pk>\d+)/$',todoedit,name='todoedit'),
    url(r'^delete/(?P<pk>\d+)/$',tododelete,name='tododelete'),

    

    
    

]