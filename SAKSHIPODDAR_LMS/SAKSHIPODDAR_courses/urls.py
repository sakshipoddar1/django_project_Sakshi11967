from django.urls import path
from . import views
urlpatterns= [
    path("signup/",views.SAKSHIPODDAR_lmsSignupUser.as_view()),
    path("getAllUser/",views.SAKSHIPODDAR_lmsGetUserDetails.as_view()),
    path("updateEmail/",views.SAKSHIPODDAR_lmsUpdateEmail.as_view()),
    path("deleteUser/<number>/",views.SAKSHIPODDAR_lmsDeleteUser.as_view()),
]