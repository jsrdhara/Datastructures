# Selection Sort

def SelectionSort(mylist):
    for fillslot in range(len(mylist)-1,0,-1):
        positionmax = 0
        for location in range(1,fillslot+1):
            if mylist[location]>mylist[positionmax]:
                positionmax = location
        temp = mylist[fillslot]
        mylist[fillslot] = mylist[positionmax]
        mylist[positionmax]=temp
    return mylist
print(SelectionSort([54,26,93,17,77,31,44,55,20]))