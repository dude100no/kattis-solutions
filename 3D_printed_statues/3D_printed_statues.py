import time


n = int(input("Enter number of statues: "))

start_time = time.time()

no_days = 0
printer_list = [0]

def statueCheckFunc(n, arr):
    for e in arr:
        if e >= n:
            return False
    return True

while statueCheckFunc(n, printer_list):
    for printer_index in range(len(printer_list)):
        printer_list[printer_index] += (printer_index + 1)
    printer_increase_num = len(printer_list)
    printer_list += [0] * len(printer_list)
    for printer_index in range(1, printer_increase_num):
        printer_list[printer_increase_num + printer_index - 1] += (printer_increase_num - printer_index)

    no_days += 1

print(len(printer_list))
print(no_days)
print(time.time() - start_time)