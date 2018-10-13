def medianSorted(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    lenComb = len1+len2
    medIndex = lenComb/2
    finalIndex = []
    isEven = False
    if(lenComb % 2 == 0):
        isEven = True
    i = 0
    j = 0
    while(i+j < len1+ len2 - 2):
        if(list1[i] <= list):
            finalIndex[i+j] = list1[i]
            j += 1
        else:
            finalIndex[i+j] = list1[j]
            i += 1
        if i + j == medIndex:
            if isEven == False:
                return finalIndex[i+j]
        if i + j == medIndex+1:
            if isEven:
                return (finalIndex[i+j-1] + finalIndex[i+j])/2

list1 = [1,2,4]
list2 = [2,4,6]
print(medianSorted(list1, list2))
