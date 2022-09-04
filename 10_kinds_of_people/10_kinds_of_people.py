h, w = list(map(lambda x: int(x), input().split(" ")))

matrix = []

for i in range(h):
    matrix.append(list(input()))

def color_check(mtx, x, y):
    if x >= 0 and y >= 0 and y < h and x < w:
        if mtx[y][x] == type_:
            return True
    return False

def floodfill(mtx, x, y):
    queue = [[x,y]]
    mtx[y][x] = f'{type_}{color_no}'
    while queue != []:
        x1, y1 = queue.pop()
        if color_check(mtx, x1, y1 + 1):
            queue.append([x1, y1 + 1])
            mtx[y1 + 1][x1] = f'{type_}{color_no}'
        if color_check(mtx, x1, y1 - 1):
            queue.append([x1, y1 - 1])
            mtx[y1 - 1][x1] = f'{type_}{color_no}'
        if color_check(mtx, x1 + 1, y1):
            queue.append([x1 + 1, y1])
            mtx[y1][x1 + 1] = f'{type_}{color_no}'
        if color_check(mtx, x1 - 1, y1):
            queue.append([x1 - 1, y1])
            mtx[y1][x1 - 1] = f'{type_}{color_no}'

color_no = 1

type_ = matrix[0][0]
floodfill(matrix, 0, 0)
for y in range(h):
    for x in range(w):
        if matrix[y][x] in ('0', '1'):
            type_ = matrix[y][x]
            color_no += 1
            floodfill(matrix, x, y)

for i in range(int(input())):
    h1, w1, h2, w2 = list(map(lambda x: int(x) - 1, input().split(" ")))
    if matrix[h1][w1] != matrix[h2][w2]:
        print("neither")
    else:
        if matrix[h1][w1] == matrix[h2][w2]:
            print("binary" if matrix[h1][w1][0] == '0' else "decimal")   
        else: print('neither')