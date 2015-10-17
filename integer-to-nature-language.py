# convert the integer to the nature langage
# use the python 3.5

def speak_number(numbers, size, base_weight):

    NUMBERS = ("one", "two",
               "three", "four",
               "five", "six",
               "seven", "eight",
               "nine")
    SUB_WEIGHTS_1 = ("ten", "eleven",
                     "twelve", "thirteen",
                     "fourteen", "fifteen",
                     "sixteen", "seventeen",
                     "eighteen", "nineteen")
    SUB_WEIGHTS_2 = ("twenty", "thirty",
                     "forty", "fifty",
                     "sixty", "seventy",
                     "eighty", "ninety")
    WEIGHTS = ( "",
                SUB_WEIGHTS_1,
                SUB_WEIGHTS_2,
                "hundred",
                "thousand",
                "million",
                "billion")

    words = ""
    part = 0
    while numbers:
        elem = numbers.pop()
        if 3 == size:
            if 0 == elem:
                pass
            else:
                words += NUMBERS[elem-1] + " " + WEIGHTS[size] + " and "
        elif 2 == size:
            if 0 == elem:
                pass
            elif 1 == elem:
                part = elem # use the sub_weight_1
            else:
                words += WEIGHTS[size][elem-2] + " " # use the sub_weight_2
        elif 1 == size:
            if part:
                words += WEIGHTS[part][elem] + " "
                part = 0
            else:
                if 0 == elem:
                    pass
                else:
                    words += NUMBERS[elem-1] + " "
        else:
            pass
        size -= 1

    base_weight += 4
    if base_weight >= 6:
        words += WEIGHTS[6] + " "
    elif base_weight >= 4:
        words += WEIGHTS[base_weight] + " "

    return words

def integer_to_nature_language(val):

    elements = []
    while val:
        elements.append(val % 10)
        val = val // 10

    all_language = ""
    base_weight = -1
    while elements:
        if len(elements) >= 3:
            speak_list = elements[:3]
            del elements[:3]
        else:
            speak_list = elements[:]
            del elements[:]
        language_piece = speak_number(speak_list, len(speak_list), base_weight)
        all_language = language_piece + all_language
        base_weight += 1


    return all_language

def main():

    print("""

        this program show how to use the nature languge to speak the number:

        example:

            123: one hundred and twenty two

    """)

    val = 123
    speak = integer_to_nature_language(val)
    print(val, ": ", speak)

    val = 782345
    speak = integer_to_nature_language(val)
    print(val, ": ", speak)

    val = 234566908
    speak = integer_to_nature_language(val)
    print(val, ": ", speak)


if __name__ == '__main__':
    main()
