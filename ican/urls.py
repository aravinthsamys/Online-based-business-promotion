from django.urls import path,include,re_path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.index,name='index'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout_page/',views.logout_page,name='logout_page'),
    path('service/',views.service,name='service'),
    path('profile',views.profile,name='profile'),
    path('alldatas',views.alldatas,name='alldatas'),
    path('alljobs',views.alljobs,name='alljobs'),
    path('fulldetails/<int:id>/',views.fulldetails,name='fulldetails'),
path('delete_jobdetails/<int:id>',views.delete_jobdetails,name='delete_jobdetails'),
    path('delete_details/<int:id>',views.delete_details,name='delete_details'),
    path('edit_fulldetails/<int:id>',views.edit_fulldetails,name='edit_fulldetails'),

    path('fulluserdata/<int:id>',views.fulluserdata,name='fulluserdata'),
    path('createpost/',views.createpost,name='createpost'),
    path('register',views.register,name='register'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('jobprofile',views.jobprofile,name='jobprofile'),
    path('jobsubmission/',views.jobsubmission,name='jobsubmission'),
]

