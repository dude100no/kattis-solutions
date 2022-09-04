values = input("").split(" ")
values = [int(i) for i in values]
values.sort()
letters = input("")
result = ["", "", ""]
for l_index in range(3):
    if letters[l_index] == "A":
        result[l_index] = str(values[0])
    elif letters[l_index] == "C":
        result[l_index] = str(values[2])
    else: result[l_index] = str(values[1])

print(result[0], result[1], result[2], sep = " ")
