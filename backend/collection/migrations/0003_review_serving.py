# Generated by Django 2.0.2 on 2018-03-31 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20180329_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='serving',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reviews', to='collection.Serving'),
        ),
    ]