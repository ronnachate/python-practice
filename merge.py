from itertools import chain
flatten = chain.from_iterable

def merge_range(ranges):
    # add offset to force stop value to low order while sorted
    stop_offset = 1
    start_flag = 1
    stop_flag = -1

    #sorted range to rearrange time with start or end flag
    ranges = sorted(flatten(((start, start_flag), (stop + stop_offset, stop_flag))
            for start, stop in ranges))
    c = 0
    result = []
    #loop all list of start and stop
    for value, flag in ranges:
        #c = 0, start new range
        if c == 0:
            start = value
        c += flag
        if c == 0:
            #need to substract stop_offset from stop value
            stop = value - stop_offset
            result.append((start, stop))
    return result


output = merge_range([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print(output)