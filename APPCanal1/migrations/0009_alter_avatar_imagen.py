# Generated by Django 4.1.2 on 2022-11-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPCanal1', '0008_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='media/avatares/usuario.png', null=True, upload_to='avatares', verbose_name='Avatar'),
        ),
    ]
