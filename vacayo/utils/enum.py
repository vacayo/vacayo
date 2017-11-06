# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import inspect


class Enum(object):
    def __init__(self):
        pass

    @classmethod
    def to_dict(cls):
        attributes = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
        attributes = filter(lambda a: not a[0].startswith('__') and not a[0].endswith('__'), attributes)
        return dict(attributes)

    @classmethod
    def to_list(cls):
        return cls.to_dict().values()

    @classmethod
    def contains(cls, value):
        if not value:
            return False

        attributes = [v.lower() for v in cls.to_list()]
        return value.lower() in attributes

    @classmethod
    def match(cls, value):
        if not value:
            return None

        attributes = {a.lower(): a for a in cls.to_list()}
        return attributes.get(value.lower())

    @classmethod
    def choices(cls):
        values = cls.to_list()
        return tuple(zip(values, values))
