# Author: O98K


class Node(object):
    def __init__(self, node, left, right):
        self._node = node
        self._left = left
        self._right = right

    @property
    def node(self):
        return self._node

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right


