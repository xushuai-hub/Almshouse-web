import datetime

from django.db import models


# Create your models here.

class oldperson_info(models.Model):
    ID = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(null=True)
    CLIENT_ID = models.IntegerField(null=True)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    birthday = models.DateField()
    checkin_date = models.DateField()
    checkout_date = models.DateField(null=True)
    imgset_dir = models.CharField(max_length=200, null=True)
    profile_photo = models.CharField(max_length=200, null=True)
    room_number = models.CharField(max_length=50, null=True)
    firstguardian_name = models.CharField(max_length=50)
    firstguardian_relationship = models.CharField(max_length=50)
    firstguardian_phone = models.CharField(max_length=50)
    firstguardian_wechat = models.CharField(max_length=50)
    secondguardian_name = models.CharField(max_length=50)
    secondguardian_relationship = models.CharField(max_length=50)
    secondguardian_phone = models.CharField(max_length=50)
    secondguardian_wechat = models.CharField(max_length=50)
    health_state = models.CharField(max_length=50)
    DESCRIPTION = models.CharField(max_length=200, null=True)
    ISACTIVE = models.CharField(max_length=10, null=True)
    CREATED = models.DateField(auto_now=True)
    CREATEBY = models.IntegerField()
    UPDATED = models.DateField(null=True)
    UPDATEBY = models.IntegerField(null=True)
    REMOVE = models.CharField(max_length=1, null=True)


class employee_info(models.Model):
    id = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(null=True)
    CLIENT_ID = models.IntegerField(null=True)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    birthday = models.DateField()
    hire_date = models.DateField()
    resign_date = models.DateField(null=True)
    imgset_dir = models.CharField(max_length=200, null=True)
    profile_photo = models.CharField(max_length=200, null=True)
    DESCRIPTION = models.CharField(max_length=200, null=True)
    ISACTIVE = models.CharField(max_length=10, null=True)
    CREATED = models.DateField(auto_now=True)
    CREATEBY = models.IntegerField()
    UPDATED = models.DateField(null=True)
    UPDATEBY = models.IntegerField(null=True)
    REMOVE = models.CharField(max_length=1, null=True)


class volunteer_info(models.Model):
    id = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(null=True)
    CLIENT_ID = models.IntegerField(null=True)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    birthday = models.DateField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    imgset_dir = models.CharField(max_length=200, null=True)
    profile_photo = models.CharField(max_length=200, null=True)
    DESCRIPTION = models.CharField(max_length=200,null=True)
    ISACTIVE = models.CharField(max_length=10, null=True)
    CREATED = models.DateField(auto_now=True)
    CREATEBY = models.IntegerField()
    UPDATED = models.DateField(null=True)
    UPDATEBY = models.IntegerField(null=True)
    REMOVE = models.CharField(max_length=1, null=True)


class event_info(models.Model):
    id = models.AutoField(primary_key=True)
    event_type = models.IntegerField()
    event_date = models.DateTimeField(auto_now=datetime.datetime.now().replace(microsecond=0))
    event_location = models.CharField(max_length=200)
    event_desc = models.CharField(max_length=200)
    oldperson_name = models.CharField(max_length=50)
    face_list = models.JSONField(null=True)


class sys_user(models.Model):
    ID = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(null=True)
    CLIENT_ID = models.IntegerField(null=True)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    REAL_NAME = models.CharField(max_length=50, null=True)
    SEX = models.CharField(max_length=20, null=True)
    EMAIL = models.CharField(max_length=50, null=True)
    PHONE = models.CharField(max_length=50, null=True)
    MOBILE = models.CharField(max_length=50, null=True)
    DESCRIPTION = models.CharField(max_length=200, null=True)
    ISACTIVE = models.CharField(max_length=10, null=True)
    CREATED = models.DateField(auto_now=True)
    CREATEBY = models.IntegerField(null=True)
    UPDATED = models.DateField(null=True)
    UPDATEBY = models.IntegerField(null=True)
    REMOVE = models.CharField(max_length=1, null=True)
    DATAFILTER = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=45, null=True)
    defaultpage = models.CharField(max_length=45, null=True)
    logoimage = models.CharField(max_length=45, null=True)
    qqopenid = models.CharField(max_length=100, null=True)
    appversion = models.CharField(max_length=10, null=True)
    jsonauth = models.CharField(max_length=1000, null=True)
