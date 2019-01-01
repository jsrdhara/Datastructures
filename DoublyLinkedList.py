class Node():

    def __init__(self,data):
        self.data = data
        self.prev=None
        self.next=None

    def get_prev(self):
        return self.prev

    def set_prev(self,prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

class DLinkedList():

    def __init__(self):
        self.head=None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_prev(temp)
        self.head = temp

    def insert_after(self, prev_node, data):

        if prev_node is None:
            print('previous note cannot be None')
            return

        new_node = Node(data)
        new_node.set_next(prev_node.next)
        prev_node.set_next(new_node)
        new_node.set_prev(prev_node)

        if new_node.get_next()!=None:
            new_node.get_next().set_prev(new_node)

    def append(self,item):

        new_node = Node(item)
        new_node.set_next(None)
        if self.head is None:
            new_node.set_prev(None)
            self.head=new_node
        last_node = self.head
        while last_node.get_next()!=None:
            last_node=last_node.get_next()
        last_node.set_next(new_node)
        new_node.set_prev(last_node)


    def print(self):
        current = self.head
        while current!=None:
            print(current.get_data())
            current=current.get_next()

mylist = DLinkedList()

mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.insert_after(mylist.head, 8)
mylist.append(7)

mylist.print()