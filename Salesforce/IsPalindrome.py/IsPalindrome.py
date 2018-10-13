def palindrome(str1):
    if len(str1) == 0:
        return False
    isPali = False
    i = 0
    j = len(str1) - 1
    while(j >= i):
        if(str1[i] != str1[j]):
            isPali = False
            return isPali
        else:
            isPali = True
        i += 1
        j -= 1
    return isPali


print(palindrome("heleh"))
