import numpy
from numpy import matrix

def editDistance(word1, word2):
    n = len(word1);

    m = len(word2);
    print("m="+str(m))
    isSame = False

    edit = numpy.zeros(shape=(m+1,n+1))
    for i in range(n+1):
        edit[0][i] = i
    for i in range(m+1):
        edit[i][0] = i

    print(edit)
    print(edit.shape)


    for i in range(1,n+1):
        for j in range(1,m+1):
            if(word1[i-1] == word2[j-1]):
                edit[i][j] = edit[i-1][j-1];
            else:
                edit[i][j] = min(edit[i-1,j] + 1, edit[i,j-1]+1, edit[i-1][j-1]+2)
            print(edit[i][j])
    print(edit)
    print(int(edit[n-1, m-1]))
    return int(edit[n-1][m-1])

word1 = "Kllo"
word2 = "Hillo"
editDistance(word1, word2)
