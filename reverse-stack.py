# use python 3.4

def insert_at_bottom(stack, value):
    if not stack:
        stack.append(value)
    else:
        current = stack.pop()
        insert_at_bottom(stack, value)
        stack.append(current)

def reverse(stack):
    if stack:
        current = stack.pop()
        reverse(stack)
        insert_at_bottom(stack, current)

def main():

    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)

    print("source stack is: ", stack)

    reverse(stack)

    print("after inverse: ", stack)


if __name__ == '__main__':
    main()
