# Generated by Django 4.1.4 on 2022-12-17 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_friend_profile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('msg_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_receiver', to='chatapp.profile')),
                ('msg_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to='chatapp.profile')),
            ],
        ),
    ]