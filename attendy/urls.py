from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'attendy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'attendy_app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^teacher_view/$', 'attendy_app.views.teacher_view', name='teacher_view'),

    url(r'^admin/', include(admin.site.urls)),
)
