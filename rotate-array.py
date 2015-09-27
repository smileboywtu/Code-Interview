# this program will rotate the array
# use the Python 3.5

def rotate_1(v, shift):
    "use the bubble sort way"
    for time in range(shift%len(v)):
        # index in assending order
        for index in range(len(v), 1, -1):
            # shift the last to first each time
            v[index-1], v[index-2] = v[index-2], v[index-1]

def reverse(v, start, end):
    "reverse the order inner array"
    while start < end:
        v[start], v[end] = v[end], v[start]
        start += 1
        end -= 1

def rotate_2(v, shift):
    "another space and time saving way"
    part = len(v) - shift%len(v)
    # reverse
    reverse(v,    0,   part-1)
    reverse(v, part, len(v)-1)
    reverse(v,    0, len(v)-1)

# test the func
a = [e for e in range(10)]

print("source array: ", a)

rotate_2(a, len(a)+1)
print("rotate ", len(a)+1, "times", a)

rotate_1(a, 3)
print("rotate using bubble sort: shift 3, ", a)

rotate_2(a, 2)
print("rotate using reverse sort: shift 2, ", a)

input("\n\nPress Enter to exit.")
