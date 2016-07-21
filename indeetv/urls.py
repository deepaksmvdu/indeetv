from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login_req', views.login_req, name='login_req'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^logout_user', views.logout_user, name='logout_user'),

    url(r'^mediafiles/(?P<user_id>\w+)/(?P<filename>[\w.\s]{0,256})$', views.mediaitems, name='mediaitems'),
    
]