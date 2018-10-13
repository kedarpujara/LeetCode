def LongestFilePath(s):
    splitS = s.split('\n')
    depthMap = {}
    currLen = 0
    maxLen = 0
    for str in splitS:
        key = depth(str)
        if(isFile(str)):
            length = sum([dict[j] for j in depthMap.keys() if j<key]) + len(getFile(str)) + key
            longest = max(longest, length)
        else:
            val = getFile(str)
            depthMap[key] =  val
    print longest
    return longest



def depth(str1):
    depth = 0
    for i in range(len(str1)):
        if str1[i:i+1] == "\t":
            depth = depth+1
            i = i+2
    return depth

def getFile(str1):
    return str1[depth(str1):]


def isFile(str1):
    if "." in str1:
        return True
    return False


LongestFilePath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
