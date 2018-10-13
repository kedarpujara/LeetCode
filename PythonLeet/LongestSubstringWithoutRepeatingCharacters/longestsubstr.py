        #pw
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        substr = ""
        max_substr = ""
        i = 0
        dict1 = {}
        while i < len(s):
            if s[i] not in dict1:
                substr = substr + s[i]
                dict1[s[i]] = i
                i = i+1
                if len(substr) > len(max_substr):
                    max_substr = substr
            else:
                i = dict1[s[i]]+1
                substr = ""
                dict1 = {}
        print max_substr
        return len(max_substr)
    # def length_enumerate(self, s):
    #     for i,letter in enumerate(s):
    #         print i
    #         print letter
    #         print ""
def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("cbbd"))
    #s.length_enumerate("help")

main()
