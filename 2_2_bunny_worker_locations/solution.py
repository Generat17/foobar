def solution(x, y):
    layer = x + y - 1
    total =  layer * (layer - 1) // 2
    return str(total + x)