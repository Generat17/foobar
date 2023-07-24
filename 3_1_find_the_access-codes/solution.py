def solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count

if __name__ == '__main__':
    ar = [1, 2, 3, 4, 5, 6]
    print(solution(ar))
