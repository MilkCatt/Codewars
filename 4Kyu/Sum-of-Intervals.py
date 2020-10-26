def sum_of_intervals(intervals):
    total = set()
    for interval in intervals:
        for x in range(interval[0], interval[1]):
            total.add(x)
            
    return len(total)