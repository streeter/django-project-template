from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    # Error pages
    url(r'^401', TemplateView.as_view(template_name='401.html'), name='401'),
    url(r'^404', TemplateView.as_view(template_name='404.html'), name='404'),
    url(r'^500', TemplateView.as_view(template_name='500.html'), name='500'),

    # Static pages
    url(r'^robots.txt$', TemplateView.as_view(),
        {'template': 'static/robots.txt', 'mimetype': 'text/plain'},
        name='robots.txt'),

    # Admin site
    url(r'^admin/', include(admin.site.urls)),
)


def handler500(request):
    return render(request, '500.html')
