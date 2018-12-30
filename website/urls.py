from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.base, name='base'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^register', views.register, name="register"),
    url(r'^new-test', views.new_test, name="new_test"),
    url(r'^create-test/(?P<name>\w+)/$', views.create_test, name="create_test"),
    url(r'^add_questions', views.add_questions, name="add_questions"),
    url(r'^new-question/(?P<name>\w+)/$', views.new_questions, name="new_questions"),
    url(r'^start-test/(?P<name>\w+)/(?P<pk>\d+)/$', views.start_test, name="start_test"),
]