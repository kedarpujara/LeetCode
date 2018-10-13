def compare(version1,version2):
    length = 0
    v1 = version1.split('.')
    v2 = version2.split('.')
    if len(v1) >= len(v2):
        length = len(v1)
    else:
        length = len(v2)
        
    for i in range(length):
        print(i)
        if i < len(v1) and i < len(v2):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                continue
        elif i < len(v1):
            if v1[i] > 0:
                return 1
        elif i < len(v2):
            if v2[i] > 0:
                return -1
    return 0

print(compare("01", "1"))
if int("01") == int("1"):
    print True
else:
    print False