# use python 3.5 as default
# insert interval

def insert_interval(intervals, insert):
    "insert into intervals"
    data = []
    insert_start, insert_end = insert

    for (start, end) in intervals:
        if start > insert_end:
            data.append((start, end))
        elif end < insert_start:
            data.append((start, end))
        elif start <= insert_end or end >= insert_start:
            insert_start = min(start, insert_start)
            insert_end   = max(end, insert_end)
        else:
            pass

    data.append((insert_start, insert_end))
    return data

def main():

    print("""

        Given a set of non-overlapping A sorted intervals, insert a new
        interval into the intevals(merge if necessary)

    """)

    intervals = [(1,2), (3,5), (6,7), (8,10), (12,15)]
    insert = (4, 9)

    print("intervals: ", intervals)
    print("insert: ", insert)

    intervals = insert_interval(intervals, insert)

    print("after insert: ", intervals)

if __name__ == '__main__':
    main()
