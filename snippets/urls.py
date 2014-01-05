from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

# Enable the ability to pass serializization patterns
# e.g.  /snippets/.json will return JSON
# or /snippets/.api will show an API view
urlpatterns += format_suffix_patterns(urlpatterns)