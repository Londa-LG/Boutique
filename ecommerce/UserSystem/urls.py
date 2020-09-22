from django.urls import path
from .views import Register_View, Login_View, Logout_View

app_name = 'User'

urlpatterns = [
    path('', Login_View, name='login'),
    path('Register/', Register_View, name='register'),
    path('Logout/', Logout_View, name='logout')
]
