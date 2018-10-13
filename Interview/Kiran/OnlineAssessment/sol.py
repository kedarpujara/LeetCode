class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # corner cases: first is leetcode-specific, second is to deal with invalid inputs.
        if not s:
            return 0
        elif s[0] == "0":
            return 0

        # num_decodings[i] corresponds to the number of ways to decode s[i:]
        num_decodings = [0] * (len(s)+1)

        # initialize base cases
        num_decodings[len(s)] = 1
        num_decodings[len(s)-1] = 1 if s[-1] != "0" else 0

        # iterate over the input, backwards
        for i in reversed(range(len(s)-1)):

            # 0 has no mapping to a letter, so we skip it.
            if s[i] == "0": continue

            num_decodings[i] = num_decodings[i+1]
            if int(s[i:i+2]) <= 26:
                num_decodings[i] += num_decodings[i+2]

        return num_decodings[0]


if __name__ == "__main__":
    for i in ["12", "0", "10", "103", "1032", "10323"]:
        print Solution().numDecodings(i)



        # isDouble = isValid(doubleDigit)
        # curr = []
        # if(isDouble):
        #   for j in range(len(possib[fullStrPrev])):
        #       if possib[fullStrPrev][j] != None:
        #           curr.append(possib[fullStrPrev][j] + alphabet[str(i)])
        #   if len(fullStrPrev2) == 0:
        #       curr.append(alphabet[doubleDigit])
        #   elif len(fullStrPrev2) > 0:
        #       for k in range(len(possib[fullStrPrev2])):
        #           if possib[fullStrPrev2][k] != None: 
        #               curr.append(possib[fullStrPrev2][k] + alphabet[str(doubleDigit)])                           
        #   possib[fullStr] = curr
        # else:
        #   for j in range(len(possib[fullStrPrev])):
        #       if possib[fullStrPrev[j] != None]:
        #           curr.append(possib[fullStrPrev][j] + alphabet[str(i)])


    # alpha = {}
    # alpha["1"] = "a"
    # alpha["2"] = "b"
    # alpha["3"] = "c"
    # alpha["4"] = "d"
    # alpha["5"] = "e"
    # alpha["6"] = "f"
    # alpha["7"] = "g"
    # alpha["8"] = "h"
    # alpha["9"] = "i"
    # alpha["10"] = "j"
    # alpha["11"] = "k"
    # alpha["12"] = "l"
    # alpha["13"] = "m"
    # alpha["14"] = "n"
    # alpha["15"] = "o"
    # alpha["16"] = "p"
    # alpha["17"] = "q"
    # alpha["18"] = "r"
    # alpha["19"] = "s"
    # alpha["20"] = "t"
    # alpha["21"] = "u"
    # alpha["22"] = "v"
    # alpha["23"] = "w"
    # alpha["24"] = "x"
    # alpha["25"] = "y"
    # alpha["26"] = "z"
    