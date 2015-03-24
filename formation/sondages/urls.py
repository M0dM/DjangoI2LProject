from django.conf.urls import patterns, include, url
from .views import index, detail, resultats, voter, DetailView

urlpatterns = \
    patterns('',
             url(r'^$', index, name='index'),

             # ?P<nom_param> permet de nommer un groupe
             # dans une expression régulière en django
             url(r'^question/(?P<pk>\d+)/detail/$',
                 DetailView.as_view(), name='detail'),
             url(r'^question/(?P<id>\d+)/resultats/$',
                 resultats, name='resultats'),
             url(r'^voter/(?P<id>\d+)$',
                 voter, name='voter'),
             )
