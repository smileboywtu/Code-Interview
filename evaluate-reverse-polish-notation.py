# this program evaluate the polish expression
# use the Python 3.5

def valueofpolish(expression):
    "evaluate the polish expression"
    stack = []
    for elem in expression:
        if elem == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif elem == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif elem == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif elem == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
        else:
            stack.append(float(elem))

    return stack.pop()

# main function
print("""

    this program evaluate the polish expression

""")
rawexpression = input("input the string: ")

polish = rawexpression.split(' ')

#polish = (2, 3, '+', 5, '*')

print("polish: ", polish)

print("value of polish is: ", valueofpolish(polish))

input("\n\nPress Enter to exit")
