class Solution(object):
    
    def isValid(s):
        closed = {"{": "}", "(": ")", "[": "]"}
        
        stack = Stack()
        stack.push(s[0])
        i = 1
        
        while(stack.isEmpty() == False):
            if self.isOpen(s[i]):
                stack.push(closed[s[i]])
                i += 1
            else:
                curr = stack.pop()
            # elif self.isClosed(s[i]):
            #     curr = stack.pop()
            #     if s[i] != curr:
            #         return False
            #     else:
            #         i += 1
        return True
        
        
    
    def isOpen(self, c):
        open_chars = ["(", "[", "{"]
        if c in open_chars:
            return True
        else:
            return False
    
    def isClosed(self, c):
        closed_chars = ["}", ")", "]"]
        if c in closed_chars:
            return True
        else:
            return False

def main():
    s = Solution()
    print(s.isValid("()"))