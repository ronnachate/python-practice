import timeit
from timeit import Timer
from itertools import chain
flatten = chain.from_iterable

def merge_range(ranges):
    result = []
    if( len(ranges) > 1):
        # add offset to force stop value to low order while sorted
        stop_offset = 1
        start_flag = 1
        stop_flag = -1

        #sorted range to rearrange time with start or end flag
        ranges = sorted(flatten(((start, start_flag), (stop + stop_offset, stop_flag))
                for start, stop in ranges))
        c = 0
    
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


def merge_range2(ranges):
    if len(ranges) > 1:
        #sorted ranges by start time
        ranges = sorted(ranges, key=lambda range: range[0])
        index = 0
        for range in ranges:
            if range[0] > ranges[index][1]:
                index += 1
                ranges[index] = range
            else:
                if range[1] > ranges[index][1]:
                    ranges[index] = (ranges[index][0], range[1])
        return ranges[:index+1]
    else:
        return ranges

output = merge_range2([(1, 5), (6,7), (2, 3)])
print(output)
output = merge_range2([(1, 10), (2, 6), (3, 5), (7, 9)])
print(output)
output = merge_range2([(6, 8), (1, 9), (2, 4), (4, 7)])
print(output)