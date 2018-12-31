class queue():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

#  Simulation: Hot Potato

def hotPotato(numlist, num):

    q = queue()
    for i in numlist:
        q.enqueue(i)

    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

