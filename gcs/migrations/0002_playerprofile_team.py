# Generated by Django 3.2 on 2023-11-15 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gcs', '0001_createsuperuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('teamid', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=40, unique=True)),
                ('user1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='playerprofile_team1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='playerprofile_team2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='playerprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerprofile_team1', to='gcs.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerprofile_team2', to='gcs.team')),
                ('team3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playerprofile_team3', to='gcs.team')),
            ],
        ),
    ]