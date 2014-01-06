from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from . import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet_detail'),

    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),
)


# Enable the ability to pass serializization patterns
# e.g.  /snippets/.json will return JSON
# or /snippets/.api will show an API view
urlpatterns += format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)