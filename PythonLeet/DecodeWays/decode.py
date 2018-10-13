class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        length = len(s)

        dp = [0]*(length+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,length):
            t1 = 0
            t2 = 0
            curr = s[i-1]
            prev = s[i-2]
            if curr != '0':
                t1 = dp[i-1]
            
            #if prev == '1' and curr >= '0' and 
    def sumNumbers(self, root):
    

    def df

def main():
    s = Solution()
    s.numDecodings("1226")

main()
# a = "12"
# print(len(a[2:]))

