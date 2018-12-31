def anagramSolution1(s1,s2):
    
    list_2 = list(s2)
    i = 0
    stillOK = True
    while i < len(s1) and stillOK:
        j = 0
        found = False
        while j < len(list_2) and not found:
            if s1[i] == list_2[j]:
                found = True
            else:
                j = j + 1
        if found:
            list_2[j] = None
        else:
            stillOK = False
        i = i + 1
    return stillOK

print(anagramSolution1('abcd','dcba'))

# second method

def anagr(a1,a2):

    list1= list(a1)
    list2 = list(a2)
    list1.sort()
    list2.sort()
    pos =0
    found = True
    while pos<len(list1) and found:
        if list1[pos]==list2[pos]:
            pos = pos +1
        else:
            found = False
    return found

print(anagr('abc','cba'))
