from django.db import models


# Create your models here.

class Url(models.Model):
    url_name = models.CharField(max_length=128)


class Roles(models.Model):
    Roles_name = models.CharField(max_length=16)


class UserInfo(models.Model):
    username = models.CharField(max_length=16)


class RolesToUrl(models.Model):
    roles = models.ForeignKey('Roles', on_delete=models.CASCADE)
    urls = models.ForeignKey('Url', on_delete=models.CASCADE)


class UserToRoles(models.Model):
    user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    roles = models.ForeignKey('Roles', on_delete=models.CASCADE)
