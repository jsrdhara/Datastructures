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
