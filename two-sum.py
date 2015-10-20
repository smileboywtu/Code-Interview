# two sum
# use the python 3.5

def two_sum(A, target):

    need = {}
    first = 1
    second = 1
    indices = range(len(A))
    for index in indices:
        if A[index] in need:
            first += need.get(A[index])
            second += index
            break
        else:
            need[target - A[index]] = index

    return first, second

def main():

    print("""

        Give an array of integers, find two numbers such that they add up
        to a specific target number.

        The function two_sum should return indices of the two numbers such
        that they add up to the target where index1 must be less than index2.
        Please note that your returned answers are not zero-based.

    """)

    A = [1, 3, 6, 34, 9, 45]
    target = 10
    print("Array: ", A)
    print("Target: ", target)

    first, second = two_sum(A, target)

    print("first: ", first, "second: ", second)


if __name__ == '__main__':
    main()
