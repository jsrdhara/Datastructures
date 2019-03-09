# Bubble sort
def BubbleSort(mylist):
    for passnum in range(len(mylist)-1,0,-1):
        for i in range(passnum):
            if mylist[i]>mylist[i+1]:
                temp=mylist[i]
                mylist[i]=mylist[i+1]
                mylist[i+1]=temp
    return mylist
print(BubbleSort([54,26,93,17,77,31,44,55,20]))

