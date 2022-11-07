# Generated by Django 4.1.3 on 2022-11-07 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomad', '0006_businesstype_remove_user_businesstype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends_score',
        ),
        migrations.RemoveField(
            model_name='user',
            name='global_score',
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_score', models.IntegerField(default=0)),
                ('friends_score', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='nomad.user')),
            ],
        ),
    ]