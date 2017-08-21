from django.conf.urls import url
from . import views
# 第二个参数表示将请求转到views.post_list函数， 第三个参数为URL命名

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),  # (?P<pk>[0-9]+)把括号里的东西转变成pk的变量并传递给view
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
