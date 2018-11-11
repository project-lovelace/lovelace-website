from django.urls import path
from django.views.generic.base import RedirectView

from .views import EditUserProfileView, ViewUserProfileView

app_name = 'users'

urlpatterns = [
    # ex: /users/
    path('', RedirectView.as_view(url='/'), name='index'),

    # Editing your own user profile, ex: /users/editprofile/
    path('editprofile/', EditUserProfileView.as_view(), name='editprofile'),

    # Viewing user profiles. ex: /users/CodeSlaya69420/
    path('<str:username>/', ViewUserProfileView.as_view(), name='profile'),
]
