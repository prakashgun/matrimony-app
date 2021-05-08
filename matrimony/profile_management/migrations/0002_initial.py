# Generated by Django 3.2 on 2021-05-08 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interest',
            name='from_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_profile_profile_set', to='profile_management.profile'),
        ),
        migrations.AddField(
            model_name='interest',
            name='to_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_profile_profile_set', to='profile_management.profile'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_management.state'),
        ),
        migrations.AddField(
            model_name='caste',
            name='religion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_management.religion'),
        ),
        migrations.AlterUniqueTogether(
            name='shortlist',
            unique_together={('from_profile', 'to_profile')},
        ),
        migrations.AlterUniqueTogether(
            name='interest',
            unique_together={('from_profile', 'to_profile')},
        ),
    ]