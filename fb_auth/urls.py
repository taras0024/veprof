from django.urls import path

from fb_auth import views

urlpatterns = [
    path('sign-in/', views.SignInView.as_view()),
    path('dj-users/', views.GetUsersView.as_view({'get': 'list'})),
]
