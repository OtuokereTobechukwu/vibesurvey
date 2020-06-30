# Generated by Django 3.0.1 on 2020-06-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createquestion',
            name='title',
            field=models.TextField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='createquestion',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
