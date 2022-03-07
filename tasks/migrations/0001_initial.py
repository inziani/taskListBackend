# Generated by Django 4.0.3 on 2022-03-07 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=32)),
                ('description', models.CharField(default='Task Details', max_length=132)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateChanged', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('dateCreated',),
            },
        ),
    ]
