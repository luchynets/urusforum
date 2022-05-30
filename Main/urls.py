from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name = "main"),
    url(r'^post/(?P<id>\d+)', views.post, name = "post"),
    url(r'^addpost', views.add_post, name = "addpost"),
    url(r'^login', views.user_login, name = "login"),
    url(r'^logout', views.user_logout, name = "logout")
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)