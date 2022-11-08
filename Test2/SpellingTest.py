import sys

def spelling_test(s, l):
    
    index_list = list(s)

    index_list.sort()

    for row in range(len(l)-1):
        for col in range(len(l)):

            temp = l[row] + l[col]
            temp_list = list(temp)
            temp_list.sort()

            if temp_list == index_list:
                return True
    return False

"""     wordset = set()
    for index in range(len(s)):
        wordset.add(s[index])


    closest_wordset = set()
    for string in l:
        substringset = set()
        for index in range(len(string)):
            substringset.add(string[index])
        if wordset.issuperset(substringset):
            closest_wordset.update(substringset)
    if wordset == closest_wordset:
        return True
    else:
        return False """

def spelling_test_helper(s, l):
    pass

def main():
    s = input()
    lines = sys.stdin.readlines()

    print(spelling_test(s, [line.replace('\n', '') for line in lines]))

if __name__ == "__main__":
    main()
