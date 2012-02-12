from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.views.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^401', TemplateView.as_view(template_name='401.html'), name='401'),
    url(r'^404', TemplateView.as_view(template_name='404.html'), name='404'),
    url(r'^500', TemplateView.as_view(template_name='500.html'), name='500'),
    url(r'^robots.txt$', direct_to_template,
        {'template': 'static/robots.txt', 'mimetype': 'text/plain'},
        name='robots.txt'),
    
    url(r'^admin/', include(admin.site.urls)),
)
