# Generated by Django 3.2.5 on 2021-07-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='celular_number',
            field=models.CharField(default='', max_length=11),
        ),
    ]
