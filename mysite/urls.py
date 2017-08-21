from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # 写正则表达式时，记得把一个r放在字符串的前面。

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),  # 把访问 'http://127.0.0.1:8000/' 的请求转到 blog.urls
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
