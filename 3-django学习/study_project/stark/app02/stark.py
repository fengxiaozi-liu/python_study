from starkComponent.service.stark import site, StarkHandler
from app02 import models


class HostHandler(StarkHandler):
    display_list = ['id', 'host', 'ip', StarkHandler.display_edit, StarkHandler.display_del]


class RoleHandler(StarkHandler):
    display_list = ['id', 'title', StarkHandler.display_edit, StarkHandler.display_del]


site.register(models.Host, HostHandler)
site.register(models.Role, RoleHandler)
