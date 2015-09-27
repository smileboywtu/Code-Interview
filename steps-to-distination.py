# find all the way to the destination
# use the python 3.5 as default

def stepforward(steps, distination):
    "step forward by one or two"
    if distination == 0:
        for step in steps:
            print(step, end=' ')
        print()
    if distination > 0:
        # move forward one
        steps.append(1)
        stepforward(steps.copy(), distination-1)
        # remove and re-forward
        steps.pop()
        # move forward two
        steps.append(2)
        stepforward(steps.copy(), distination-2)

# main func here
print("find all the road to the distination: ")

step = []
stepforward(step, 10)

input("\n\nPress Enter to exit.")
