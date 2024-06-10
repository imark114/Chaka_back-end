from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationViewSet.as_view(), name='register'),
    path('active/<uid64>/<token>/', views.activate, name='activate'),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('contact/', views.ContactCreateView.as_view(), name='contact-create'),
    path('profile/', views.UserProfileViewSet.as_view(), name='profile'),
]
