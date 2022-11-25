# Generated by Django 4.1.2 on 2022-11-15 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APPCanal1', '0019_perfil_alter_avatar_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='avatar',
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='avatares', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=''),
        ),
    ]
