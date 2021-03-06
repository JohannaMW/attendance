from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = patterns('',
    # App
    url(r'^$', 'attendy_app.views.home', name='home'),
    url(r'^get_mayor/$', 'attendy_app.views.get_mayor', name='get_mayor'),

    # User authentication
    url(r'^register/$', 'attendy_app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^teacher_view/$', 'attendy_app.views.teacher_view', name='teacher_view'),
    url(r'^check_in/$', 'attendy_app.views.check_in', name='check_in'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
