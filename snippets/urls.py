from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet_detail'),
)

# Enable the ability to pass serializization patterns
# e.g.  /snippets/.json will return JSON
# or /snippets/.api will show an API view
urlpatterns += format_suffix_patterns(urlpatterns)