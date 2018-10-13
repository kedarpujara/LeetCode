def partitionLabels(s):
    """
    :type S: str
    :rtype: List[int]
    """
    #Go through and add to dicitonary
    #Do overlapping intervals

    dict1 = {}
    for i in range(len(s)):
        if s[i] not in dict1:
            dict1[s[i]] = [i]
            dict1[s[i]].append(0)
        else:
            dict1[s[i]][1] = i #set max index to higher i
        print(dict1[s[i]])
    print dict1
    intervals = []
    for interval in dict1:
        intervals.append(dict1[interval])
    curr_lo = 10000
    curr_max = 0

    for interval in intervals:
        if interval[0] < curr_lo:
            curr_lo = interval[0]
        elif interval[]
    print intervals

partitionLabels("ababcbacadefegdehijhklij")
