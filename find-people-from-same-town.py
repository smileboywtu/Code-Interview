# find the people from the same town
# use python 3.5 as default

"""
    How to find the people from the same home town?

        Xiao Ming is a new colleage student, he wants to know who is from the
    same town as him. But many people just tell him that he or she is from the
    same town with another student.

    Can you find the all the people from the same town with XiaoMing?

    Demo:
        if 4 people invoved in the dialog
        there are 3 relationship told
            1 4
            3 2
            2 4

        if we just image XiaoMing is 1
        so from 1 4 we know 4 is from the same town with XiaoMing.
        from 2 4, we know 2 is from the same town with XiaoMing
        ...
        Finally we can get 2 3 4 are from the same town with XiaoMing

"""

# import
from collections import deque

class Graph(object):
    "save the undirect graph"

    def __init__(self):
        "init the graph"
        self.__graph = {}

    def __str__(self):
        "show the graph"
        return str(self.edges())

    def setSet(self, set):
        "set the key set of the graph, the key is the island actually"
        for key in set:
            self.add(key)

    def add(self, island_1, island_2=None):
        "add an edge"
        if island_2 == None:
            self.__graph[island_1] = []
        else:
            self.__graph[island_2].append(island_1)
            self.__graph[island_1].append(island_2)

    def edges(self):
        "return all the edges contained in the map"
        edges = []
        for key in self.__graph:
            for island in self.__graph[key]:    # not empty
                edges.append((key, island))

        return edges

    def isolate(self):
        "return just the isolate island"
        isolate = []

        for island in self.__graph:
            if not self.__graph[island]:
                isolate.append(island)

        return isolate

    def relate(self, island_3):
        "find the other islands related to island_3"
        visit = []
        queue = deque([])

        queue.append(island_3)

        while queue:

            current = queue.popleft()

            if current not in visit:
                visit.append(current)
                for relate in self.__graph[current]:
                    if relate not in queue:
                        queue.append(relate)

        return visit

def findship(set, people, ship):
    "find all the relationship of people"
    relation = Graph()
    # set first
    relation.setSet(set)
    # add
    for edge in ship:
        a, b = edge
        relation.add(a, b)

    # find
    return relation.relate(people)

def main():
    "simple demo"
    print("""

            Find People From Same Town

        N   -- number of people invoved in dialog
        M   -- number of ship got

        if n = 0 and m =0 just quit the program

        Example:

            input:
                5 4
                1 3
                1 5
                2 4
                3 5
                0 0

            output:
                2
    """)

    while 1:

        n, m = input().split()

        n = int(n)
        m = int(m)

        if n == 0 and m == 0:
            break

        ship = []
        while m:
            a, b = input().split()
            ship.append((int(a), int(b)))
            m -= 1

        ships = findship(range(n), 0, ship)
        print(ships)


if __name__ == '__main__':
    main()
