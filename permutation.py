# this program will list the permutation
# use python 3.5 as default

"""
                      / 1,2{3} --- 1,2,3
            / 1{2, 3}
          /           \ 1,3{2} --- 1,3,2
        /
{1,2,3} ----- 2{1,3}
        \
          \
            \ 3{1,2}
"""

def permutationiterator(set, start, end, choose):
    "permutate the choose members"
    if start is choose:
        for index in range(choose):
            print(set[index], end=' ')
        print()
    else:
        for index in range(start, end): # notice here: start index is start
            # swap the index with the start
            set[start], set[index] = set[index], set[start]
            # forward to get another one
            permutationiterator(set.copy(), start+1, end, choose)
            # swap back and try another
            set[start], set[index] = set[index], set[start]

def permutation(m, n):
    "permutation n number in group of m members"
    #set = list(range(m))
    set = [i+1 for i in range(m)]
    permutationiterator(set, 0, m, n)

# main func
print("""

    permutation using recursive method

    A(3, 2):
            1, 2
            1, 3
            2, 3
            2, 1
            3, 1
            3, 2

""")

m = 3
n = 3 

print("choose n=", n, "in total m=", m, "members")

permutation(m, n)

input("\n\nPress Enter to exit.")
