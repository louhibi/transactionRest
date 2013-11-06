from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from front import views

urlpatterns = patterns('',
    url(r'^transaction/$', views.TransactionList.as_view()),
    url(r'^transaction/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
    url(r'^client/$', views.ClientList.as_view()),
    url(r'^client/(?P<pk>[0-9]+)/$', views.ClientDetail.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)