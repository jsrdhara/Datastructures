def InsertionSort(mylist):
    for index in range(1,len(mylist)):
        position = index
        currentvalue = mylist[index]
        while position>0 and mylist[position-1]>currentvalue:
            mylist[position]=mylist[position-1]
            position=position-1

        mylist[position]=currentvalue
    return mylist

print(InsertionSort(([54,26,1])))