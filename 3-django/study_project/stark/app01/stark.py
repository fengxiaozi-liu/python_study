from starkComponent.service.stark import site, StarkHandler
from app01 import models
from django import forms


class DepartmentHandler(StarkHandler):
    display_list = ['id', 'title', StarkHandler.display_edit, StarkHandler.display_del]


class UserInfoHandler(StarkHandler):
    display_list = ['id', 'name', 'age', 'email', StarkHandler.get_choices_text('性别', 'gender'),
                    StarkHandler.display_edit, StarkHandler.display_del]

    fields = ['id', 'name', 'age', 'gender', 'email']

    def save(self, form, is_update=False):
        form.instance.depart_id = 3
        form.save()


site.register(models.Department, DepartmentHandler)
site.register(models.UserInfo, UserInfoHandler)
