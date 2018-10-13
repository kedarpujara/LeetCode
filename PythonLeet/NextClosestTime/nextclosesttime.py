s = "19:34"
def next_closest(s):
    a = nums_available(s)
    for i in range(len(s)-1,0,-1):
        for num in a:
            if num()

def nums_available(s):
    a = []
    for i in range(len(s)):
        if s[i] != ':' and s[i] not in a:
            a.append(int(s[i]))
    return a

def get_hours_minutes(s):
    s = s.split()
    return s[0], s[1]


def is_valid_time(hours, mins):
    int_hours = int(hours)
    int_mins = int(mins)
    if int_hours >= 0 and int_hours <= 23 and int_mins >= 0 and int_mins <= 59:
        return True
    return False