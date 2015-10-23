from django.conf.urls import patterns, url
from ajax import changeFormHandler


urlpatterns = patterns('',
    url(r'^change_form/$', changeFormHandler, name='changeFormHandler'),
)