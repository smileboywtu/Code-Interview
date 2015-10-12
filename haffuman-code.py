# how to build the haffuman code
# use the python 3.5

class TreeNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

def haffuman_code(data):

    while len(data) > 1:

        data.sort(key=lambda node: node.val, reverse=True)

        a = data.pop()
        b = data.pop()
        newnode = TreeNode(a.val + b.val)
        newnode.left = a
        newnode.right = b

        data.append(newnode)

    return data.pop()

def pack_data(list):
    "pack the data to node"

    nodes = []
    for data in list:
        newnode = TreeNode(data)
        nodes.append(newnode)

    return nodes

def print_tree_pre(root):
    "deep first search"
    if root:
        print(root.val, end=" ")
        print_tree_pre(root.left)
        print_tree_pre(root.right)

def print_tree_mid(root):
    if root:
        print_tree_mid(root.left)
        print(root.val, end=" ")
        print_tree_mid(root.right)

def main():

    print("""

        build the haffuman code

    """)

    data = [1, 4, 3, 5, 7, 6, 9]

    print("wights: ", data)

    nodes = pack_data(data)

    root = haffuman_code(nodes)

    print("Haffuman Tree: ")
    print("pre search: ")
    print_tree_pre(root)
    print()

    print("mid search: ")
    print_tree_mid(root)
    print()

if __name__ == "__main__":
    main()
