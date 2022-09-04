def moving_left(row):
    for index in range(3):
        count = index + 1
        while True:
            if row[index] == row[count]:
                row[index] *= 2
                row[count] = 0
                # count += 1
                break
            elif row[count] != 0 or count == 3:
                break
            count += 1
    # return row
    new_row = [num for num in row if num != 0]
    new_row += [0] * (4 - len(new_row))
    return new_row

def moving_right(row):
    count = 2
    for index in range(3, 0, -1):
        count = index - 1
        while True:
            if row[index] == row[count]:
                row[index] *= 2
                row[count] = 0
                break
            elif row[count] != 0 or count == 0:
                break
            count -= 1

    new_row = [num for num in row if num != 0]
    new_row = [0] * (4 - len(new_row)) + new_row

    return new_row

def moving_down(col):
    count = 2
    for index in range(3, 0, -1):
        count = index - 1
        while True:
            if col[index] == col[count]:
                col[index] *= 2
                col[count] = 0
                break
            elif col[count] != 0 or count == 0:
                break
            count -= 1

    new_col = [num for num in col if num != 0]
    new_col = [0] * (4 - len(new_col)) + new_col
    return new_col

def moving_up(col):
    count = 1
    for index in range(3):
        count = index + 1
        while True:
            if col[index] == col[count]:
                col[index] *= 2
                col[count] = 0
                break
            elif col[count] != 0 or count == 3:
                break
            count += 1

    new_col = [num for num in col if num != 0]
    new_col += [0] * (4 - len(new_col))
    return new_col

# matrx = [[2,0,0,2],[4,16,8,2],[2,64,32,4],[1024,1024,64,0]]
# matrx = [[2,2,4,8],[4,0,4,4],[16,16,16,16],[32,16,16,32]]

matrx = []
for row in range(4):
    row_input = input("").split()
    # print(row_input)
    row_int = list(map(lambda x: int(x), row_input))
    matrx.append(row_int)

move_dir = int(input("")) # 0 - left, 1 - up, 2 - right, 3 - down
if move_dir == 0: # left
    for i_row in range(4):
        matrx[i_row] = moving_left(matrx[i_row])
elif move_dir == 1: # up
    for i_col in range(4):
        col = []
        for i_row in range(4):
            col.append(matrx[i_row][i_col])
        new_col = moving_up(col)
        for i_e in range(len(new_col)):
            matrx[i_e][i_col] = new_col[i_e]
elif move_dir == 2: # right
    for i_row in range(4):
        matrx[i_row] = moving_right(matrx[i_row])
else: # down
    for i_col in range(4):
        col = []
        for i_row in range(4):
            col.append(matrx[i_row][i_col])
        new_col = moving_down(col)
        for i_e in range(len(new_col)):
            matrx[i_e][i_col] = new_col[i_e]

for row in matrx:
    print(row[0], row[1], row[2], row[3], sep = " ")