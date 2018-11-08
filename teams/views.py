from django.shortcuts import render, redirect

from django.contrib.auth.models import User

# Create your views here.
from django.views import generic
from .models import Team
import re
class TeamView(generic.ListView):
    template_name = 'teams.html'
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        return Team.objects.filter(users=self.request.user)

class TeamViewUserTeam(generic.ListView):
    template_name = 'teams_user.html'
    def get_queryset(self):
        teamId = int(re.search('[0-9]+', self.request.path).group(0))
        return User.objects.filter(team__id=teamId)
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        
        teamId = int(re.search('[0-9]+', self.request.path).group(0))

        if not list(Team.objects.filter(id=teamId)[0].users.all()).__contains__(self.request.user):
            return redirect('/teams/')

        return super(TeamViewUserTeam, self).dispatch(request, *args, **kwargs)