"""
Whiteboarded attempt for algorithm 
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lo = 0
        hi = len(s)-1

        while lo < hi:
            if s[lo] == s[hi]:
                #At lo and hi, this is palindrome 
                #Find which one is further from beginning 
                if self.is_pal(s[lo:hi+1]):
                    if self.distance(0,lo) < self.distance(hi,len(s)-1):
                        s = s[hi::-1] + s 
                    elif self.distance(0,lo) > self.distance(hi,len(s)-1):
                        return 0
                    
        return 0


    def distance(self, start, end):
        return end-start



    def is_pal(self, s):        
        if s == s[::-1]:
            return True         
        return False

def main():
    s = Solution()
    st = "abacdddcaba"
    #print(st[3:])
    print(s.is_pal(st))
main()
