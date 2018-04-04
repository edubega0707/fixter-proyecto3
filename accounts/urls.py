from django.urls import path
from .views import ProfileView, CreateUser, EditProfile
from django.contrib.auth import views as logViews


app_name='accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name="profile"),
    path('registro/',  CreateUser.as_view(), name="registro"),
    path('login/', logViews.login, name='login'),
    path('logout/', logViews.logout, name='logout'),
    path('edit/', EditProfile.as_view(), name='edit')

]
