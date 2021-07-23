from django.db import models

class GateWay(models.Model):
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name="网关名称")
    topic = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name="网关主题")
    gateway_id = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name="网关ID")
    location = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        unique=True,
        verbose_name="网关位置")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "app_gateway"


