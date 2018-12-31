class  Dequeue():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self,item):
        self.items.insert(0,item)

    def addFront(self,item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# palindrome checker

def palchecker(aString):
    chardeque = Dequeue()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))


def palchecke(aString):
    chardeque = []

    for ch in aString:
        chardeque.append(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.pop()
        last = chardeque.pop(0)
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecke("lsdkjfskf"))
print(palchecke("radar"))
