percentage_list = []
for class_ in range(int(input(""))):
    score_list_str = input("").split(" ")
    score_list = [int(score_list_str[i]) for i in range(len(score_list_str)) if i != 0]
    no_stu = int(score_list_str[0])
    avg = sum(score_list) / no_stu

    abv_avg = 0
    for score in score_list:
        if score > avg:
            abv_avg += 1

    percent_abv_avg = round(abv_avg / no_stu * 100, 3)

    percentage_list.append(percent_abv_avg)

for percent in percentage_list:
    percent = str(percent)
    count = 0
    add = False
    for e in percent:
        if e == ".":
            add = True
        elif add:
            count += 1

    if count < 3:
        percent += "0" * (3 - count)
    print(f"{percent}%")