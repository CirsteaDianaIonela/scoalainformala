from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('new_account/', views.CreateNewAccount.as_view(), name='utilizator_nou'),
    path('start_timesheet/', views.newtimesheet, name='start_pontaj'),
    path('stop_timesheet/', views.stoptimesheet, name='stop_pontaj'),
]
