import logging
import sys

from urllib.parse import urlencode


from connection import Connection

from resources import Auth, IPOMaster, Transactions, Notification, EForms, Ncb


log = logging.getLogger("nse.api")


class NseIPO(object):
    def __init__(self, access_token=None, env="uat"):
        self.env = env
        self.access_token = access_token
        self.connection = Connection(env, access_token)

    def __getattr__(self, item):
        return ResourceWrapper(item, self.connection)


class ResourceWrapper(object):
    def __init__(self, resource_cls, conn_obj):
        self.conn_obj = conn_obj
        self.resource_class = self.str_to_class(resource_cls)

    def __getattr__(self, item):
        return lambda *args, **kwargs: (getattr(self.resource_class(self.conn_obj), item))(*args, **kwargs)

    @classmethod
    def str_to_class(cls, resource):
        return getattr(sys.modules[__name__], resource)
