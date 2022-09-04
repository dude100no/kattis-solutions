import sys

for line in sys.stdin:
    two_num_str = line.split(" ")
    two_num = [int(i) for i in two_num_str]
    print(abs(two_num[0] - two_num[1]))