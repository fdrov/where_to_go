# Generated by Django 3.2.3 on 2021-05-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(default=0,
                                                   verbose_name='Позиция фото'),
        ),
    ]
