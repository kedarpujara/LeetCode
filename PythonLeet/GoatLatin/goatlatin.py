"""
Conditions
1. Word begins w/vowel 
    - append m + (index*a)
2. Word begins with consanant 
    - move first letter to end of word 
    - append m + (index*a)

"""
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:return ""
        words = S.split()

        for i in range(len(words)):
            if self.is_vowel(words[i]):
                suffix = self.add_suffix(i,False, words[i])
            else:
                suffix = self.add_suffix(i,True, words[i])                
            words[i] = suffix
        print(words)
        return " ".join(words)
        

    def is_vowel(self, s):        
        vowels = 'AEIOU'
        if s[0].upper() in vowels:
            return True
        else:
            return False

    def add_suffix(self, i, consonant, s):
        if consonant:
            s = s[1:] + s[:1]
        suffix = s + "m" + "a"*(i+2)            
        return suffix

def main():
    s = Solution()
    s.toGoatLatin ("The quick brown fox jumped over the lazy dog")
main()