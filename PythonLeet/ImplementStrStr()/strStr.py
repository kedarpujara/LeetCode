class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or haystack == needle:
            return 0
        j = len(needle)
        i = 0
        return_index = -1
        while j <= len(haystack):
            if haystack[i:j] == needle:
                return_index = i
                break
            else:
                i = i+1
                j = j+1
        return return_index
