# urls.py in your 'accounts' app
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup,profile
from django.contrib import admin


app_name = 'accounts'
urlpatterns = [
    # other URL patterns
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('signup', signup, name='signup'),
    path('profile', profile, name='profile'),
]
    # path('admin/', admin.site.urls),



