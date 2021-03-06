# Generated by Django 3.1.7 on 2021-03-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('board', '0002_auto_20210308_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '게시글', 'verbose_name_plural': '게시글'},
        ),
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag', verbose_name='태그'),
        ),
    ]
