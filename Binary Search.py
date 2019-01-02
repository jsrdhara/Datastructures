# Implementation of Binary Search

#Iterative Method

def BinarySearch(mylist,item):
    first = 0
    last = len(mylist)-1
    found = False
    while first<=last and not found:
        mid = (first+last)//2
        if mylist[mid]==item:
            found=True
        else:
            if item<mylist[mid]:
                last = mid-1
            else:
                first=mid+1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(BinarySearch(testlist, 17))
print(BinarySearch(testlist, 13))

# Recursive Method

def rBinarySearch(mylist,item):

    if len(mylist)==0:
        return False
    else:
        mid = len(mylist)//2
        if mylist[mid]==item:
            return True
        else:
            if item<mylist[mid]:
                return rBinarySearch(mylist[:mid], item)
            else:
                return rBinarySearch(mylist[mid+1:], item)

print(rBinarySearch(testlist, 17))
print(rBinarySearch(testlist, 13))


