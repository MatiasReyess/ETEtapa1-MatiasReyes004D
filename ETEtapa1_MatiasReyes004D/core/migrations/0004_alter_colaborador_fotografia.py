# Generated by Django 3.2.3 on 2021-07-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_colaborador_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='Fotografia',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
