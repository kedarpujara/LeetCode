def longest_palindrome(s):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    diff = 0
    substr = ""
    max_substr = ""
    # if not s[10]:
    #     print True
    for i in range(1,len(s)):
        #Check odd
        substr = s[i]
        while (i - diff) >= 0 and (i+diff) < len(s) and s[i-diff] == s[i+diff]:
            substr = s[i-diff:i+diff+1]
            #print(substr)
            diff = diff + 1
        #max_substr = max(len(max_substr), len(substr))
        if len(substr) > len(max_substr):
            max_substr = substr



    diff = 0
    substr = ""
    print("max")
    print(max_substr)
    for i in range(1,len(s)):
        #Check even
        while (i - diff) >= 0 and (i+diff) < len(s) and s[i-diff-1] == s[i+diff]:
            # print("one")
            # print(s[i-diff-1])
            # print("two")
            # print(s[i+diff])
            substr = s[i-diff-1:i+diff+1]
            #print substr
            #print(substr)
            diff = diff+1
        #max_substr = max(len(max_substr), len(substr))
        if len(substr) > len(max_substr):
            max_substr = substr
    print("max")
    return max_substr






print(longest_palindrome("abcdbbfcba"))
