# Generated by Django 3.0.2 on 2020-06-18 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=20)),
                ('priority', models.CharField(max_length=5)),
                ('police_allotted', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_slot', models.CharField(max_length=10)),
            ],
        ),
    ]
