# regular expression match
# use python 3.5 as default

def is_match(str0, pattern):
    "match the str with pattern"
    if 0 == len(pattern):
        return 0 == len(str0)

    if 1 == len(pattern):
        if len(str0) < 1:
            return False
        elif pattern[0] != str0[0] and pattern[0] != '.':
            return False
        else:
            return 1 == len(str0)

    if '*' != pattern[1]:
        if len(str0) < 1:
            return False
        elif pattern[0] != str0[0] and pattern[0] != '.':
            return False
        else:
            return is_match(str0[1:], pattern[1:])
    else:
        # '*' stands for 0 elements
        if is_match(str0, pattern[2:]):
            return True
        # '*' stands for 1 or more preceding elements
        i = 0;
        while i < len(str0) and (str0[i] == pattern[0] or pattern[0] == '.'):
            if is_match(str0[i+1:], pattern[2:]):
                return True
            i += 1
        return False

def main():

    print("""

                Regular Expression Matching

        implement regular expression matching with support
        for '.' and '*'

        Here you just need to deal with the special case:

            if pattern is empty, just judge if string is empty

            if pattern is one, just judge if the length and element match

            if pattern is two, deal with the second element is '*' or not '*'

            other case, use recursive method to slice the question

    """)

    # test
    print("str: aab, pattern: c*a*b*, result: ", is_match("aab", "c*a*b*"))
    print("str: aa, pattern: .*, result: ", is_match("aa", ".*"))
    print("str: aa, pattern: a, result: ", is_match("aa", "a"))


if __name__ == '__main__':
    main()
