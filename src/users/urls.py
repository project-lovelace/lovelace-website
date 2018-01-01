from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'users'

urlpatterns = [
    # ex: /users/
    path('', RedirectView.as_view(url='/'), name='index'),

    # ex: /users/CodeSlaya69420/
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
]
