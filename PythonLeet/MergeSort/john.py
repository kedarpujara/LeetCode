def merge(L, R):
    l = r = 0
    result = []
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            result.append(L[l])
            l += 1
        else:
            result.append(R[r])
            r += 1
    result.extend(R[r:])
    result.extend(L[l:])
    return result

def mergeSort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2

    left = mergeSort(A[:mid])
    right = mergeSort(A[mid:])

    return merge(left, right)

ar = [2,4,1,6,8,5,3,7]

print(mergeSort(ar))