# Generated by Django 4.2.3 on 2023-11-10 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodels',
            name='Category',
            field=models.CharField(choices=[('Hurrur', 'hurrur'), ('mistry', 'mistry'), ('humar', 'humar'), ('ci fi', 'ci fi')], default='hurrur', max_length=30),
        ),
        migrations.AddField(
            model_name='bookmodels',
            name='first_pub',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmodels',
            name='last_pub',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
