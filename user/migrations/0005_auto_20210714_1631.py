# Generated by Django 3.2.4 on 2021-07-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_name_volunteer_info_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sys_user',
            name='CLIENT_ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='CREATEBY',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='DATAFILTER',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='DESCRIPTION',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='ISACTIVE',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='ORG_ID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='REMOVE',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='UPDATEBY',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='UPDATED',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='appversion',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='defaultpage',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='jsonauth',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='logoimage',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='qqopenid',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sys_user',
            name='theme',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
