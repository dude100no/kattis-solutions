# def moving_left(row):
#     count = 1
#     for index in range(3):
#         if count == index: continue
#         while True:
#             if row[index] == row[count]:
#                 row[count] *= 2
#                 row[index] = 0
#                 count += 1
#                 break
#             elif row[count] != 0 or count == 3:
#                 break
#             count += 1
#     # return row
#     new_row = [num for num in row if num != 0]
#     new_row += [0] * (4 - len(new_row))
#     return new_row

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

print(moving_left([32, 16, 16, 32]))