# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'portal.views',
    url(r'^$', 'home', name='home'),
    url(r'^access/$', 'access', name='access'),
    url(r'^logout/$', 'user_logout', name='logout'),
    url(r'^witty/$', 'witty', name='witty'),
    url(r'^historico_alunos/$', 'historicos', name='historicos'),
    url(r'^alterar_senha/$', 'alterar_senha', name='alterar_senha'),
    url(r'^disciplinas/', include('disciplina.urls')),
    url(r'^perfil/', include('pessoa.urls')),
)
