# Given two almost identical lists of worker IDs x and y where one of the lists contains an additional ID, write a function solution(x, y) that compares the lists and returns the additional ID.
#
# For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function solution(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't.
# Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], the function solution(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.
#
# In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99,
# and one of the lists will contain an additional unique integer which should be returned by the function. The same n non-unique integers will be present on both lists,
# but they might appear in a different order like in the examples above. Commander Lambda likes to keep the numbers short, so every worker ID will be between -1000 and 1000.

class solution:
    def solution(x, y):
        if (len(x) > len(y)):
            res = sum([i for i in x]) - sum([i for i in y])
        else:
            res = sum([i for i in y]) - sum([i for i in x])

        return res


if __name__ == "__main__":
    print(solution.solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))
    print(solution.solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))