from django.conf.urls import patterns, include, url
from one_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', views.index, name='one'),
)
