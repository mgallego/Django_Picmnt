from django.conf.urls import patterns, include, url
from picmnt.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_picmnt.views.home', name='home'),
    # url(r'^django_picmnt/', include('django_picmnt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
                       #(r'^$', main_page),
                       (r'^$', random_image), #temp, for test 
                       (r'^random/$', random_image),


)
