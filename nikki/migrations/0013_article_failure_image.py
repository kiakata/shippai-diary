# Generated by Django 2.0.5 on 2018-06-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nikki', '0012_merge_20180607_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='failure_image',
            field=models.CharField(max_length=20, null=True, verbose_name='失敗の画像イメージ'),
        ),
    ]
