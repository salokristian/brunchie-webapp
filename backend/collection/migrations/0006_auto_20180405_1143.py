# Generated by Django 2.0.2 on 2018-04-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20180401_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='buffetmenu',
            name='name',
            field=models.CharField(default='Tasty buffet', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serving',
            name='system',
            field=models.IntegerField(choices=[(1, 'Ala carte'), (2, 'Buffet'), (3, 'Buffet and Ala carte')]),
        ),
    ]