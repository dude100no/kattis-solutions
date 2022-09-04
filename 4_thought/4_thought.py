op_list = ["+", "-", "*", "//"]
no_lines = int(input(""))
no_list = []
eqn_list = []
for no_i in range(no_lines):
    number = int(input(""))
    no_list.append(number)


for op_1 in op_list:
    for op_2 in op_list:
        for op_3 in op_list:
            eqn = f"4{op_1}4{op_2}4{op_3}4"
            eqn_list.append([eqn, eval(eqn)])

for num in no_list:
    if -60 <= num <= 256:
        for eqn, result in eqn_list:
            no_sol = True
            if result == num:
                eqn = eqn.replace("//", "/")
                print(f"{eqn} = {result}")
                no_sol = False
                break
        if no_sol:
            print("no solution")
    else:
        print("no solution")