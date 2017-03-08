from django.conf.urls import patterns, include, url
from apps.hello import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^request_list/$', views.request_list, name='request_list'),
    url(r'^request_list_ajax/$',
        views.request_list_ajax,
        name='request_list_ajax'),
)
