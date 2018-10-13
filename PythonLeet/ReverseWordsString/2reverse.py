class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        curr_word = ""
        words = []
        for char in str: 
            if char != " ":
                curr_word += char 
            else:
                if curr_word != "":
                    words.append(curr_word)
                    curr_word = ""
        words.append(curr_word)
        rev_s = " ".join(words[::-1])
        res = []
        for char in rev_s:
            res.append(char)
        return res 

    
            




def main():
    s = Solution()
    a = [2, "2"]
    print(a)
    sentence = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    print(s.reverseWords(sentence))
main()