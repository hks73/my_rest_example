"""my_rest_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import restapp.views
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),  #Go to admin page and fill the db
    url(r'^get/(?P<id>\d+)/$',restapp.views.userDetails), #get show the full information of user
    url(r'^User/', restapp.views.userList),         #using this url we can see all user with user naem and user ids
    url(r'^post/', restapp.views.postDetails),    #put post request using form
    url(r'^delete/(?P<id>\d+)/$', restapp.views.deleteUserDetails) #Delete user object using user id
]
