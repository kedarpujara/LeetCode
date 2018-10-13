class Solution:
    def decode(self, s):
        self.alphabet = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        self.memo = [None]*(len(s)+1)
        
        return self.helper_decode_dp(s, len(s))

    

    def helper_decode_dp(self, s, k):
        
        begin = len(s)-k
        if k == 0:
            return 0
        if s[begin] == "0":
            return 0
        if self.memo[k] != None:
            return self.memo[k]
        result = self.helper_decode_dp(s, k-1)
        if k >= 2 and int(s[begin:begin+2] <= 26):
            result += self.helper_decode_dp(s,k-2)
        self.memo[k] = result 
        return result
        


    #     #Base cases handling faulty beginning and starting with zeroes
    #     if s[0] == "0":
    #         return 0
    #     elif s[len(s)-1] == 0 and s[len(s)-2] > 2:
    #         return 0
        
    #     print(s[len(s)-2])

    #     return 1
    #     while i < len(s):
    #          if s[i] != 0:



def main():
    s = Solution()
    print(s.decode("212"))
main()

