# Generated by Django 3.2.3 on 2021-05-24 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_watchlist_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together={('user', 'api_movie_id')},
        ),
    ]
