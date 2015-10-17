# list all the combination using recursive method
# use python 3.5 as default

"""
    c(4, 2):
                                    {1,2,3,4}
                                    /   |   \\
                                  /     |    \\
                            1{2,3,4}  2{3,4}  3{4}
                            /   |   \  /  \    |
                        1, 2  1,3 1,4 2,3 2,4 3,4

"""

def combinationiterator(set, start, end, current, choose):
    "iterate the elements in set"
    if current is choose:
        for index in range(choose):
            print(set[index], end=' ')
        print()
    else:
        for index in range(start, end):
            # get enough elements to choose
            if end - index >= choose - current:
                set.append(index + 1)
                # think why here just use the index + 1 not the start + 1
                combinationiterator(set.copy(), index+1, end, current+1, choose)
                set.pop()

def combination(m, n):
    "interface to create the combination list"
    set = []
    combinationiterator(set, 0, m, 0, n)

print("""

    combination using recursive method
    C(3, 2):
            1, 2
            1, 3
            2, 3
""")

m = 3
n = 2

print("choose n=", n, "in group of m=", m, "members")

combination(m, n)

input("\n\nPress Enter to exit.")
