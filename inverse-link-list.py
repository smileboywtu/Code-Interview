# inverse the link list
# use python 3.5

class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self):
        return string(self.val)

def buildlist():
    "build the list"
    head = Node()
    current = head

    for i in range(10):
        current.val = i+1
        current.next = Node(i+2)
        current = current.next

    return head

def printlist(head):
    "show the list"
    while head:
        print(head.val, end=" ")
        head = head.next

    print()

def inverse(head):
    stop = None
    current = head

    while 1:
        if stop == head:
            break
        if current.next == stop:
            stop = current
            current = head
            continue

        current.val, current.next.val = current.next.val, current.val

        current = current.next

    return head

def main():

    head = buildlist()

    print("The source list is: ")
    printlist(head)

    head = inverse(head)

    print("After inverse operation: ")
    printlist(head)


if __name__ == '__main__':
    main()
