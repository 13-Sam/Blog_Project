from django.urls import path
from App_Login import views


app_name = "App_Login"

urlpatterns = [
path('signup/', views.sign_up, name='signup'),
path('login/', views.login_page, name = 'login'),
path('logout/', views.logout_user, name='logout'),
path('profile/', views.profile, name = 'profile'),
path('change-profile/', views.user_change, name = 'user_change'),
path('password/', views.change_pass, name='change_pass'),
path('add_pro_pic/', views.add_pro_pic, name='add_pro_pic'),
]
