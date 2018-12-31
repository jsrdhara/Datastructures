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

class LinkedList():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head==None

    def add(self,item):

        current = self.head
        previous = None
        stop = False

        while current!=None and not stop:
            if current.get_data()>item:
                stop = True
            else:
                previous=current
                current = current.get_next()

        temp = Node(item)
        if previous==None:
            temp.set_next(self.head)
            self.head=temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self,item):

        current =self.head
        previous = None
        found = False

        while current!=None and not found:

            if current.get_data()==item:
                found=True
            else:
                previous=current
                current=current.get_next()

        if previous==None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())


    def reverse(self):

        current =self.head
        previous =None
        while current!=None:
            next = current.get_next()
            current.next_node=previous
            previous=current
            current=next
        self.head=previous

    def search(self,item):

        current =self.head
        found=False
        stop=False
        while current!=None and not found and not stop:
            if current.get_data()==item:
                found = True
            else:
                if current.get_data()>item:
                    stop =True
                else:
                    current=current.get_next()
        return found

    def index(self,item):

        current = self.head
        found = False
        index = 0
        while current!=None and not found:

            if current.get_data()==item:
                found=True
            else:
                current=current.get_next()
                index=index+1
        return index

    def print(self):
        current = self.head
        while current!=None:
            print(current.get_data())
            current=current.get_next()

mylist = LinkedList()
mylist.add(3)
mylist.add(2)
mylist.add(4)
mylist.print()
print('**********')
mylist.reverse()
mylist.print()
print('**********')
print(mylist.search(2))
print('**********')
print(mylist.index(2))
mylist.remove(2)
print('**********')
mylist.print()
