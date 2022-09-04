import math

input_ = input("").split(" ")
N, d, s, t, f_min, f_max = input_
# N - the number of eyelets in a column
# d - vertical distance between eyelets
# s - horizontal distance between eyelets
# t - thickness of the eyelets
# f_min - the minimum remaining length of lace
# f_max - the maximum remaining length of lace

lace_len = int(input(""))

lace_len -= s
lace_len -= 2 * N * t
lace_len /= 2

eyelet_used = [0 for i in range(N)]

def lace_comb_check(eyelet_used, lace_len):
    for eyelet in eyelet_used:
        