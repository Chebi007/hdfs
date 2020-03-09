__author__ = 'Liliia'

from sys import maxsize

class Directory:

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return "\"%s\"" % (self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

