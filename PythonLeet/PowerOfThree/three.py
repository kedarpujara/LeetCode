def three(num):
    #print num ==1
    isPower = False
    print isPower
    if num == 1:
        isPower = True
    elif num % 3 != 0 and num != 1:
        isPower = False
    elif num % 3 == 0:
        three(num/3)
    return isPower
#print(three(27));

def binary():
    print 1162261467%(9)
binary()
