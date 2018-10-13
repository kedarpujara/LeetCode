class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not dict:
            return sentence
        if not sentence:
            return None 
        words = sentence.strip().split(" ")
        for i in range(len(words)):
            for prefix in dict:                
                if words[i].startswith(prefix):
                    words[i] = prefix                    
        return " ".join(words)


def main():
    s = Solution()
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(s.replaceWords(dict, sentence))

main()