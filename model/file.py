__author__ = 'Liliia'

from sys import maxsize

class File:

    def __init__(self, dir=None, id=None):
        self.dir = dir
        self.id = id

    def __repr__(self):
        return "\"%s\"" % (self.dir)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.dir == other.dir

