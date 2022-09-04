prob = {}
time = "time"
w = "wrong"
r = "right"
solved = 0
time_penalty = 0

while True:
    log_input = input("")
    if log_input == "-1":
        break
    log_list = log_input.split(" ")
    if log_list[1] not in prob:
        prob[log_list[1]] = {"wrong": 0, "right": 0}

    if not prob[log_list[1]][r] > 0:
        prob[log_list[1]][log_list[2]] += 1
        prob[log_list[1]][time] = int(log_list[0])

for problem in prob:
    if prob[problem][r] == 1:
        solved += 1
        time_penalty += prob[problem][time] + prob[problem][w] * 20

print(solved, time_penalty, sep = " ")