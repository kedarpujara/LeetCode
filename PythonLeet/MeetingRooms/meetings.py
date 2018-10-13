
def meeting_rooms(times):
    times.sort()
    print(times)
    curr_min = times[0][0]
    curr_max = times[0][1]
    num_rooms = 1
    for i in range(1,len(times)):
        print(curr_max)
        if times[i][0] < curr_max:
            print("here")
            num_rooms += 1
            curr_min = times[i][0]
            curr_max = times[i][1]
    return num_rooms


times = [[2,7],[6,12],[13,15]]
times2 = [[0, 30],[5, 10],[15, 20]]
times3 = [[7,10],[2,4]]
print(meeting_rooms(times3))