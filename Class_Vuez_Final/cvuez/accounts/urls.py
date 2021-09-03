from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome_page, name="welcome_page"),
    path('consultation_bookings/', views.consultation_booking,  name="consultation_booking"),
    path('book_consultation/', views.insert_booking, name="insert_booking"),
    path('lecturer_details/', views.lecturer_details, name="lecturer_details"),

    path('lecturer_details/', views.showdept, name="showdept"),

    path('registerLecturer.html/', views.registerLecturer_page, name="registerLec"),
    path('registerStudent.html/', views.registerStudent_page, name="registerStud"),
    path('registerAdmin.html/', views.registerAdmin_page, name="registerAdmin"),

    path('loginLecturer.html/', views.loginLecturer_page, name="loginLec"),
    path('loginStudent.html/', views.loginStudent_page, name="loginStud"),
    path('loginAdmin.html/', views.loginAdmin_page, name="loginAdmin"),

    path('logout/', views.logout_user, name="logout"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),

    path('home/', views.home, name="home"),

    path('student_details/', views.student_details, name="student_det"),
    path('class/', views.ClassInsert, name="class"),
    path('profile/', views.Profile, name="profile"),
    path('Terms_and_Conditions/',views.T_and_C,name="T_C"),
]
