# Generated by Django 5.2 on 2025-05-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_projeto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='data_contratacao',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='data_nascimento',
            field=models.DateTimeField(),
        ),
    ]
