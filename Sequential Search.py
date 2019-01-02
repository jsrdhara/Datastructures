# Sequential Searcch

def SequentialSearch(mylist,item):
    index=0
    found=False
    while index < len(mylist) and not found:
        if mylist[index] == item:
            found = True
        else:
            index = index+1
    return found

print(SequentialSearch([3,5,89,25,42],42))

# Orderedsequential Search (Numbers are ordered

def OrderedSequrntialSearch(mylist,item):
    mylist=sorted(mylist)
    found = False
    stop = False
    index=0
    while index <len(mylist) and not found and not stop:
        if mylist[index]==item:
            found =True
        else:
            if mylist[index]>item:
                stop = True
            else:
                index = index+1
    return found

print(OrderedSequrntialSearch([3,5,89,25,42],2))
