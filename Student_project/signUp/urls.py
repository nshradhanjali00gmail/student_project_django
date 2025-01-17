from django.urls import path
from . import views

urlpatterns = [
    path('', views.signUP_View , name= 'signup'),
    path('candidateSignUp/', views.candidate_SignUp_View , name= 'candidateSignUp'),
    path('requiterSignUp/', views.requiter_SignUp_View, name= 'requiterSignUp'),
    path('candidatelogin/', views.CandidateLoginView , name='candidatelogin'),
    path('recruiterlogin/', views.RecruiterLoginView , name='recruiterlogin'),
    path('login/', views.login_View, name='login'),
    path('logout/', views.logout_view, name='logout'),
]