# Generated by Django 4.2 on 2024-04-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', '남성'), ('F', '여성')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='바깡', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='self_introduction',
            field=models.TextField(blank=True),
        ),
    ]
