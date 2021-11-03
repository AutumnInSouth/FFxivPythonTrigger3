class Node(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        val = self.top.val
        self.top = self.top.next_node
        return val


class Queue(object):
    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, val):
        new_node = Node(val)
        if self.top is None:
            self.top = new_node
        else:
            self.bottom.next_node = new_node
        self.bottom = new_node

    def pop(self):
        val = self.top.val
        self.top = self.top.next_node
        return val
