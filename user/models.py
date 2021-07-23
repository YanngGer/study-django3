import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.fields import RestrictedFileField


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "avatar"
    if ext.lower() in ["pdf", "docx"]:
        sub_folder = "document"
    return os.path.join(instance.id, sub_folder, filename)


class User(AbstractUser):
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户姓名")
    avatar = RestrictedFileField(upload_to=user_directory_path, max_length=100,
                                 content_types=[
                                     'image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/tiff'],
                                 max_upload_size=5242880, default='default_avatar.png', verbose_name="用户头像")
    user_id = models.IntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户ID")
    signature = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户个性签名")
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户称呼")
    group = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户部门")
    tags = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户标签")
    notify_count = models.IntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户通知数量")
    unread_count = models.IntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户未读通知数量")
    country = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户国家")
    access = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户权限")
    geographic = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户家乡")
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户地址")
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=True,
        verbose_name="用户电话号码")

    def __str__(self):
        return self.username

    class Meta:
        db_table = "app_user"
