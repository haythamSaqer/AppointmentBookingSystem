# from django.urls import path
#
# from . import views

# urlpatterns = [
#     path('', views.HomeView.as_view(), name='home'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('book_appointment/', views.book_appointment, name='book_appointment'),
#     path('confirm_appointment/<int:appointment_id>/', views.confirm_appointment, name='confirm_appointment'),
# ]

# app_name = 'appointments'
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('book/', views.book_appointment, name='book_appointment'),
#     path('confirm/<int:pk>/', views.confirm_appointment, name='confirm_appointment'),
# ]

from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from project import settings
from .views import login_view, logout, signup, home, appointments, confirm_appointment, doctor_login, doctor_signup, patient_login, patient_signup

app_name = 'appointments'

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    # path('logout/', logout, name='logout'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('appointments/', appointments, name='appointments'),
    path('confirm_appointment/<int:pk>/', confirm_appointment, name='confirm_appointment'),

    path('doctor/login/', doctor_login, name='doctor_login'),
    path('doctor/signup/', doctor_signup, name='doctor_signup'),
    path('patient/login/', patient_login, name='patient_login'),
    path('patient/signup/', patient_signup, name='patient_signup'),
]