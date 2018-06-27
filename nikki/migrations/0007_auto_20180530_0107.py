# Generated by Django 2.0.5 on 2018-05-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nikki', '0006_auto_20180525_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_time',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_time',
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='作成日時'),
        ),
        migrations.AddField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時'),
        ),
    ]