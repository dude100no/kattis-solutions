import copy

allowables = []
allowables.append(chr(i) for i in range(65, 91))
allowables.append(chr(i) for i in range(97, 123))
allowables.append(["?", "!", ",", ".", " "])

def convert_img_border(tl_corner, h_count, w_count):
    img_count = len(img_loc)
    h = tl_corner[0]
    w = tl_corner[1]

    temp_matrix[h][w:w + w_count] = [f"+{img_count}"] * w_count
    temp_matrix[h + h_count - 1][w:w + w_count] = [f"+{img_count}"] * w_count

    for hi in range(h_count):
        temp_matrix[h + hi - 1][w] = f"+{img_count}"
        temp_matrix[h + hi - 1][w + w_count - 1] = f"+{img_count}"

H, W = map(lambda x: int(x), input().split(" "))

matrix = []


img_loc = []

for i in range(H):
    matrix.append(list(input()))

temp_matrix = copy.deepcopy(matrix)

while True:
    plus_row_loc = []
    for i in range(H):
        if '+' in temp_matrix[i]:
            plus_row_loc.append(i)

    if len(plus_row_loc) == 0:
        break

    i = 0
    while i < len(plus_row_loc):
        h = plus_row_loc[i]
        w = matrix[h].index("+")
        tl_corner = [h, w]

        h_count = 1
        w_count = 1
        while h_count < H - h:
            if matrix[h + h_count][w] != "+":
                break
            h_count += 1
        while w_count < W - w:
            if matrix[h][w + w_count] != "+":
                break
            w_count += 1

        img_loc.append([tl_corner, h_count, w_count])
        i += h_count
        convert_img_border(tl_corner, h_count, w_count)

print(temp_matrix)