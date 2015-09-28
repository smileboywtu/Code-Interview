# this program implement the binary tree in python
# use the python 3.5 as default

"""

            root
         /        \
       /           \
      left         right

"""

# import
from collections import deque

class BinaryTree():

    def __init__(self, root=None):
        self.__id = root
        self.__left = None
        self.__right = None

    def __str__(self):
        tostring = ""
        tostring += self.__id
        tostring += " "
        return tostring

    @property
    def id(self):
        "access the id directly"
        return self.__id

    def setId(self, id):
        "use to set the id of the node"
        self.__id = id

    def getLeft(self):
        "return the id of the left"
        return self.__left

    def setLeft(self, left):
        self.__left = left

    def getRight(self):
        "get the the right"
        return self.__right

    def setRight(self, right):
        "set the rifht"
        self.__right = right

    def add(self, elem):
        "add new node to the tree"
        if self.__id is None:
            self.__id = elem
        elif self.__id > elem:
            if self.__left is None:
                self.__left = BinaryTree()
            self.__left.add(elem)
        elif self.__id < elem:
            if self.__right is None:
                self.__right = BinaryTree()
            self.__right.add(elem)
        else:
            pass

    def traverse(self):
        "pre-order"
        if self is not None:
            print(self, end=' ')
            if self.__left is not None:
                self.__left.traverse()
            if self.__right is not None:
                self.__right.traverse()

    def boardtraverse(self):
        "board traverse"
        queue = deque([])
        # init the queue
        if self is not None:
            queue.append(self)

        while queue:
            current = queue.popleft()
            print(current, end=' ')
            if current.getLeft() is not None:
                queue.append(current.getLeft())
            if current.getRight() is not None:
                queue.append(current.getRight())


# main func
tree = BinaryTree()

print("""

    Binay Tree:

        Input like: "H", "D", "C", "A", "F", "E"
        
                  H
                 /
                /
               D
             /   \\
            /     \\
           C      F
          /      /
         /      /
        A      E

""")

tree.add('H')
tree.add('D')
tree.add('C')
tree.add('A')
tree.add('F')
tree.add('E')


tree.traverse()
print()
tree.boardtraverse()

input("\n\nPress Enter to exit.\n")
