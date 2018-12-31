class Node():

    def __init__(self,data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self,data):
        self.data = data

    def set_next(self,node):
        self.next_node = node

class Linkedlist():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head==None

    def add (self,item):

        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):

        current = self.head
        count =0
        while current!=None:
            count = count+1
            current=current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def index(self, item):
        current = self.head
        found = False
        count=0
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                count=count+1

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current!=None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    def reverse(self):
        prev = None
        current = self.head
        while current!=None:
            next = current.next_node
            current.next_node= prev
            prev=current
            current=next
        self.head=prev

    def print(self):
        current=self.head
        while current!=None:
            print(current.get_data())
            current=current.get_next()

mylist = Linkedlist()

mylist.add(25)
mylist.add(26)
mylist.add(27)

mylist.print()
print('/***********/')
mylist.remove(26)
mylist.print()
print('/***********/')
mylist.reverse()
mylist.print()