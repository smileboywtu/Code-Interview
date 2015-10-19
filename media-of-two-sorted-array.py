# find the media of two sorted array
# use python 3.5 as default

def find_kth_element(A, B, k, a_start, a_end, b_start, b_end):
    "find the kth element in array of two"

    a_len = a_end - a_start + 1
    b_len = b_end - b_start + 1

    if 0 == a_len:
        return B[b_start + k]
    if 0 == b_len:
        return A[a_start + k]
    if 0 == k:
        return min(A[a_start], B[b_start])

    # get mid of the two array
    a_mid_len = a_len * k // (a_len + b_len)
    b_mid_len = k - a_mid_len - 1

    a_mid = a_mid_len + a_start
    b_mid = b_mid_len + b_start

    if A[a_mid] > B[b_mid]:
        k = k - (b_mid - b_start + 1)
        a_end = a_mid
        b_start = b_mid + 1
    else:
        k = k - (a_mid - a_start + 1)
        b_end = a_mid
        a_start = a_mid + 1

    return find_kth_element(A, B, k, a_start, a_end, b_start, b_end)

def find_media_of_two_sorted_array(A, B):

    a_len = len(A)
    b_len = len(B)
    media = (a_len + b_len) // 2

    if (a_len + b_len) % 2:
        return find_kth_element(A, B, media, 0, a_len-1, 0, b_len-1)
    else:
        return (find_kth_element(A, B, media,   0, a_len-1, 0, b_len-1) + \
                find_kth_element(A, B, media-1, 0, a_len-1, 0, b_len-1)) / 2

def main():

    print("""

        There are two sorted arrays A and B of size m and n respectively.
    Find the median of the two sorted arrays. The overall run time complexity
    should be O(log(m+n)).

    Algorithm:
        1) Calculate the medians m1 and m2 of the input arrays A and B respectively
        2) If m1 and m2 are equal then we are done, and return m1 (or m2)
        3) If m1 is greater than m2, then median is present in one of the below
           two subarrays
        a) From first element of A to m1
        b) From m2 to last element of B
        4) If m2 is greater than m1, then median is present in one of the below
           two subarrays
        a) From m1 to last element of A
        b) From first elementof B to m2
        5) Repeat the above process until size of both the subarrays becomes 2.
        6) If size of the two arrays is 2 then use below formula to get the
           media.
                Median = (max(A[0], B[0]) + min(A[1], B[1])) / 2

    """)

    A = [1, 2, 3, 4, 5, 6]
    B = [4, 5, 7, 9, 11, 13, 15, 17]

    media = find_media_of_two_sorted_array(A, B)

    print("sorted array A: ", A)
    print("sorted array B: ", B)
    print("median: ", media)

if __name__ == '__main__':
    main()
