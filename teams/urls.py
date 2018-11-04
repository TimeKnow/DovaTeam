from django.urls import path, re_path
from teams import views
urlpatterns = [
    path('', views.TeamView.as_view(), name='teams'),
    re_path(r'^(?P<team_id>[0-9]+)/$', views.TeamViewUserTeam.as_view(), name='team_id'),
]