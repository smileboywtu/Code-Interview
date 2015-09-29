# word ladder
# use the python 3.5 as default

"""

    Word ladder

    How it work?

    Given two words and a dictionary, find the length of shortest transformation
    sequence from start to end, such that only one letter can be changed at a
    time and each intermidiate word must exist in the dictionary.

    start = "hit"
    end   = "cog"
    dict = ["hot", "dot", "dog", "lot", "log"]

    two to get there:

        "hit"->"hot"->"dot"->"dog"->"cog"
        "hit"->"hot"->"lot"->"log"->"cog"

    By comparing these two, we can get the shortest length is 5

"""

# import
import string
from collections import deque

def wordladder(start, end, dic):
    "find the shortest way from start to end"

    ALPHA = list(string.ascii_lowercase)

    words = deque([])       # use to save the tree word
    steps = deque([])       # use to save the step used
    track = len(dic)+3      # use to find the shortest one

    words.append(start)
    steps.append(1)

    while words:

        current = words.popleft()
        step = steps.popleft()

        # check if find the end
        if current == end:
            if track > step:
                track = step
            continue

        for index in range(len(current)):
            # try to find different possible word
            for c in ALPHA:
                # try to find the word in dict
                possible = list(current)
                possible[index] = c
                word = ''.join(possible)
                if word in dic or word == end:
                    words.append(word)
                    steps.append(step + 1)
                if word in dic:
                    dic.remove(word)

    # return the shortest one
    return track


def main():
    "for test"

    print("""

                Breath First Search

        Here we just use the breath first search to find the shortest length.

        Look at the example here:

            start: "hit"
            end  : "cog"
            dict : ["hot", "dot", "dog", "lot", "log"]

                                hit
                                 |
                                hot
                            /         \\
                          /            \\
                         dot           lot
                          |             |
                         dog           log
                          \\            /
                           \\         /
                               cog

            so here you need to use the queue to deal with this question

            1) push "hit" to queue, and 1 to queue
            2) push "dot" to queue, and 2 to queue
               push "lot" to queue, and 2 to queue
            3) ...

    """)

    start = "hit"
    end = "cog"
    dic = ["hot", "dot", "dog", "lot", "log"]

    shortest = wordladder(start, end, dic)

    print("shortest one key road is: ", shortest)

    input("\n\nPress Enter to exit.\n")


if __name__ == '__main__':
    main()
