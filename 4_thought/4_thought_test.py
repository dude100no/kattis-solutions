operators = ["+", "-", "*", "//"]
eqn_list = {}
for a in operators:
    for b in operators:
        for c in operators:
            eqn = f"4 {a} 4 {b} 4 {c} 4"
            val = eval(eqn)
            eqn = eqn.replace('//', '/')
            eqn_list[val] = f"{eqn} = {val}"

for line in range(int(input(""))):
    num = int(input(""))
    if -60 <= num <= 256 and num in eqn_list:
        print(eqn_list[num])
    else: print("no solution")