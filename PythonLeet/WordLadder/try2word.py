from collections import deque 
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        q = deque()
        q.append([beginWord, endWord])
        #print(q.pop())
        ladder = 0
        while q:
            if len(wordList) == 0:
                return 0
            curr = q.pop()
            print(curr)
            ladder += 1
            one_away_curr = []
            for val in curr:
                if val == endWord:
                    return ladder
                else:
                    one_away_curr, wordList = self.one_away(val, wordList, one_away_curr)

            q.append(one_away_curr)
        return 0

    
    def one_away(self, word, wordList, one_away):        
        count_diffs = 0
        for dict_word in wordList:
            count_diffs = 0
            print(word)
            print(dict_word)
            for c1, c2 in zip(word, dict_word):
                print(c1, c2)
                if c1 != c2:
                    count_diffs += 1
            if count_diffs <= 1:
                print(dict_word)
                one_away.append(dict_word)                
            for word in one_away:
                wordList.remove(word)
            print("")
        return one_away, wordList


def main():
    s = Solution()
    #print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    one = []
    #print(zip("dog", "hit"))
    print(s.one_away("dog", ["hot","dot","dog","lot","log","cog"], one))
main()
count_diffs = 0
for c1, c2 in zip("dog", "cog"):
    print(c1, c2)
    if c1 != c2:
        count_diffs += 1
print(count_diffs)
# if count_diffs <= 1:
#     one_away.append(dict_word)
#     wordList.remove(dict_word)