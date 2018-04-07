# Generated by Django 2.0.2 on 2018-04-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_auto_20180405_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='headline',
            field=models.CharField(default='An amazing experience!!', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='visit_type',
            field=models.IntegerField(choices=[(1, 'Friends'), (2, 'Family'), (3, 'Work'), (4, 'Couple'), (5, 'Other')], default=1),
            preserve_default=False,
        ),
    ]