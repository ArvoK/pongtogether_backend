from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.
class team(models.Model):
    teamid = models.AutoField(primary_key=True)
    user1 = models.OneToOneField(User, on_delete=models.CASCADE, related_name='playerprofile_team1')
    user2 = models.OneToOneField(User, on_delete=models.CASCADE , related_name='playerprofile_team2')
    team_name = models.CharField(max_length=40, unique=True, blank=False)

admin.site.register(team)
class playerprofile(models.Model):
    team1 = models.ForeignKey(team, on_delete=models.CASCADE, related_name='playerprofile_team1')
    team2 = models.ForeignKey(team, on_delete=models.CASCADE, related_name='playerprofile_team2')
    team3 = models.ForeignKey(team, on_delete=models.CASCADE, related_name='playerprofile_team3')

admin.site.register(playerprofile)