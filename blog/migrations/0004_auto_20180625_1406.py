# Generated by Django 2.0.5 on 2018-06-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180625_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=False, null=True),
        ),
    ]
