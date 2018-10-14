class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        num = [[0 for i in range(n)] for j in range(m)]
        num[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    num[i][j] += num[i-1][j]
                if j -1 >= 0:
                    num[i][j] += num[i][j-1]
        return num[m-1][n-1]

