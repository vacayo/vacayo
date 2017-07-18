from __future__ import unicode_literals


class Struct(object):

    def __init__(self, d):
        self.__dict__ = d

    def __hash__(self):
        return hash(tuple(self.__dict__.values()))

    def __eq__(self, other):
        return tuple(self.__dict__.values()) == tuple(other.__dict__.values())

    def __ne__(self, other):
        return not(self == other)

    def __getattr__(self, prop):
        if prop.startswith('__') and prop.endswith('__'):
            return super(Struct, self).__getattr__(prop)

        return None
