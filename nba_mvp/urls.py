
from django.urls import path
from players import views as player_views

urlpatterns = [
    path("", player_views.main, name="home")
]
