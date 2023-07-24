from collections import Counter


def buildGCDTable(n):
    result = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == 0 or j == 0:
                result[i][j] = 1
                result[j][i] = 1
            elif i == j:
                result[i][j] = i + 1
            else:
                result[i][j] = result[i][j - i - 1]
                result[j][i] = result[i][j - i - 1]
    return result


def gcd(x, y, gcdTable):
    return gcdTable[x - 1][y - 1]


def buildFactorialTable(n):
    result = [1]
    for i in range(n - 1):
        result.append(result[-1] * (i + 2))
    return result


def factorial(x, factorialTable):
    return factorialTable[x - 1]


def coefficientFactor(c, n, factorialTable):
    cc = factorial(n, factorialTable)
    for a, b in Counter(c).items():
        cc //= (a ** b) * factorial(b, factorialTable)
    return cc


def partitionsAndCycleCount(n, factorialTable):
    k = 0
    p = n * [0]
    p[0] = n
    result = []
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    result = []
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            partition = a[:k + 2]
            result.append((partition, coefficientFactor(partition, n, factorialTable)))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        partition = a[:k + 1]
        result.append((partition, coefficientFactor(partition, n, factorialTable)))
    return result


def solution(w, h, s):
    n = max(w, h)
    gcdTable = buildGCDTable(n)
    factorialTable = buildFactorialTable(n)

    grid = 0
    for cpw in partitionsAndCycleCount(w, factorialTable):
        for cph in partitionsAndCycleCount(h, factorialTable):
            m = cpw[1] * cph[1]
            grid += m * (s ** sum([sum([gcd(i, j, gcdTable) for i in cpw[0]]) for j in cph[0]]))
    return str(grid // (factorial(w, factorialTable) * factorial(h, factorialTable)))

if __name__ == '__main__':
    print(solution(2, 3, 4))