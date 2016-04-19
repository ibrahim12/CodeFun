import sys

class Node(object):
    next = None
    prev = None
    value = None

    def __init__(self, value=None):
        self.value = value

class DList(object):
    def __init__(self):
        self.length = 0
        self.root = Node()
        self.tail = Node()

        self.root.next = self.tail
        self.tail.prev = self.root

    def add(self, value):

        node = Node(value)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

        self.length += 1

    def removeByValue(self, value):
        temp = self.root.next
        while temp != self.tail and temp.value != value:
            temp = temp.next

        if temp != self.tail:

            node_to_remove = temp

            node_to_remove.prev.next = node_to_remove.next
            node_to_remove.next.prev = node_to_remove.prev

            del node_to_remove

            self.length -=  1

            return temp

        return -1

    def get_by_value(self, value):
        temp = self.root.next
        while temp != self.tail and temp.value != value:
            temp = temp.next

        return temp

    def move_to_head(self, node):

        node.prev.next = node.next
        node.next.next.prev = node.prev

        node.next = self.root.next
        node.prev = self.root
        self.root.next = node

    def remove_root(self):
        if self.root.next != self.tail:
            node_to_remove = self.root.next
            self.root.next = self.root.next.next

            return node_to_remove.value

    def p(self):
        s = "r - "
        temp = self.root.next
        while temp != self.tail:
            s +=  str(temp.value) + " - "
            temp = temp.next
        s += " t"

        print s
        print ""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.mem = {}
        self.dlist = DList()
        self.cap = capacity


    def p(self):
        self.dlist.p()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.mem:
            node = self.dlist.get_by_value(key)
            self.dlist.move_to_head(node)
            return self.mem[key]
        else:
            return -1


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if key in self.mem:
            node = self.dlist.get_by_value(key)
            self.dlist.move_to_head(node)

        elif self.dlist.length == self.cap :
            # print "L %s" %  self.dlist.length
            tail_key = self.dlist.remove_root()
            # print tail_key
            if tail_key:
                del self.mem[tail_key]

            self.dlist.add(key)
            self.mem[key] = value

        else:
           self.mem[key] = value
           self.dlist.add(key)


s = LRUCache(1)
print "--set 2, 1"
s.set(2, 1)
s.p()
print "--get 2"
print s.get(2)
s.p()
print "-- set 3, 2"
s.set(3, 2)
s.p()
print "-- get 2"
print s.get(2)
s.p()
print "-- get 3"
print s.get(3)
s.p()
