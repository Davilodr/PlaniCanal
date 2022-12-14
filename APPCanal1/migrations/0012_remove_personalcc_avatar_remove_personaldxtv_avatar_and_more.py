# Generated by Django 4.1.2 on 2022-11-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPCanal1', '0011_remove_personalcc_avatar_remove_personaldxtv_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalcc',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='personaldxtv',
            name='avatar',
        ),
        migrations.AddField(
            model_name='personalcc',
            name='avatar',
            field=models.ImageField(blank=True, default='media/avatares/usuario.png', null=True, upload_to='avatares', verbose_name='Avatar'),
        ),
        migrations.AddField(
            model_name='personaldxtv',
            name='avatar',
            field=models.ImageField(blank=True, default='media/avatares/usuario.png', null=True, upload_to='avatares', verbose_name='Avatar'),
        ),
    ]
