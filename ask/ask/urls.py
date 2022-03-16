"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
# from django.urls import include
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', include('qa.urls')),
    url(r'^login/$', include('qa.urls')),
    url(r'^signup/$', include('qa.urls')),
    url(r'^question/(?P<id>[0-9]+)/$', include('qa.urls')),
    url(r'^ask/$', include('qa.urls')),
    url(r'^popular/$', include('qa.urls')),
    url(r'^new/$', include('qa.urls')),

    # url(r'^.*$', include('qa.urls')),
    # url('^$', include('qa.urls')),
    # url(r'^admin/', admin.site.urls),
    # url('^$', 'qa.views.test'),
    # url('^login/', 'qa.views.test'),
    # url('^signup/', 'qa.views.test',),
    # url('^question/\d+/', 'qa.views.test'),
    # url('^ask/', 'qa.views.test'),
    # url('^popular/', 'qa.views.test'),
    # url('^new/', 'qa.views.test'),
]
