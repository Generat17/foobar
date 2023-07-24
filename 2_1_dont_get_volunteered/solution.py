from collections import deque


# Узел queue, используемый в BFS.
class Node:
    # (x, y) представляет координаты шахматной доски
    # `dist` представляет минимальное расстояние от источника.
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist

    # Поскольку мы используем `Node` в качестве ключа в словаре,
    # нам нужно переопределить функции `__hash__()` и `__eq__()`
    def __hash__(self):
        return hash((self.x, self.y, self.dist))

    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)


# Ниже перечислены все восемь возможных движений коня.
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]


# Проверить, являются ли (x, y) действительными координатами шахматной доски.
# Обратите внимание, что конь не может выйти за пределы доски.
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)


# Найдите минимальное количество шагов, сделанных конем.
# от источника для достижения пункта назначения с использованием BFS
def solution(src, dest):

    N = 8
    src = Node(src // 8, src % 8)
    dest = Node(dest // 8, dest % 8)

    # настроен на проверку того, посещалась ли ячейка матрицы раньше или нет
    visited = set()

    # создает queue и ставит в queue первый узел
    q = deque()
    q.append(src)

    # Цикл # до тех пор, пока queue не станет пустой
    while q:

        # удаляет передний узел из очереди и обрабатывает его
        node = q.popleft()

        x = node.x
        y = node.y
        dist = node.dist

        # , если пункт назначения достигнут, обратный путь
        if x == dest.x and y == dest.y:
            return dist

        # пропустить, если место было посещено ранее
        if node not in visited:
            # пометить текущий узел как посещенный
            visited.add(node)

            # проверка всех восьми возможных движений коня
            # и ставить в queue каждое допустимое движение
            for i in range(len(row)):
                # получить действительное положение коня из текущего положения на
                # шахматная доска и поставить ее в queue с дистанцией +1
                x1 = x + row[i]
                y1 = y + col[i]

                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))

    # возвращает бесконечность, если путь невозможен
    return 0