# Generated by Django 3.1.1 on 2020-09-17 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_follow'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('slug', 'title')},
        ),
    ]
