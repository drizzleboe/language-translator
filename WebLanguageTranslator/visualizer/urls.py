from django.urls import path
from . import views

urlpatterns=[
    path('', views.index_view, name='index' ),
    path('signup', views.signup_view, name='signup'),
    path('signin', views.signin_vew, name='signin'),
    path('signout', views.logout_view, name='logout'),
   ]