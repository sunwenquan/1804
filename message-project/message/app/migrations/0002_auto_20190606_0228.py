# Generated by Django 2.2.1 on 2019-06-06 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='address',
            field=models.CharField(default='xxxxx', max_length=50, verbose_name='地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.CharField(default='contentdfadfasdfas', max_length=200, verbose_name='留言内容'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default='adfasdfa@qq.com', max_length=20, verbose_name='邮箱'),
            preserve_default=False,
        ),
    ]
