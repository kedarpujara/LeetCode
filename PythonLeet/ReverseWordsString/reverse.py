class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split(" ")                
        i = 0
        while i < len(words):  
            while i< len(words) and words[i] == "":
                words.remove(words[i])
            i += 1
        print(words)
        return " ".join(words[::-1])


def main():
    s = Solution()
    print(s.reverseWords("   a   b "))

main()