import re
from itertools import product
from datetime import datetime, timedelta
import random

# num = ''.join(random.choice(['0', '1', '?']) for i in range(500000))
num = '1?0'

start = datetime.now()

q_indexes = [i.start() for i in re.finditer('\?', num)]
q_perms = list(product(['0', '1'], repeat=len(q_indexes)))

perm_count = 0

for perm_i in range(len(q_perms)):
    zero_count = 0
    q_count = 0
    total_zero = q_perms[perm_i].count('0') + num.count('0')
    for i in range(len(num)):
        if num[i] == '0':
            if i != zero_count:
                perm_count += i - zero_count
            zero_count += 1
        elif num[i] == '?':
            if q_perms[perm_i][q_count] == '0':
                if i != zero_count:
                    perm_count += i - zero_count
                zero_count += 1
            q_count += 1
        elif zero_count == total_zero:
            continue

print(perm_count % 1000000007)
end = datetime.now()
diff = end - start
print(diff)

# import re
# from itertools import product

# def replace_str_index(text,index=0,replacement=''):
#     return f'{text[:index]}{replacement}{text[index+1:]}'

# # num = '10?101?1010??110'
# # num = '?0?'
# num = '101000100101'
#       #000000011111

# q_indexes = [i.start() for i in re.finditer('\?', num)]
# q_perms = list(product(['0', '1'], repeat=len(q_indexes)))

# perm_count = 0

# for perm_i in range(len(q_perms)):
#     temp_num = num
#     for q_i in range(len(q_indexes)):
#         temp_num = replace_str_index(temp_num, q_indexes[q_i], q_perms[perm_i][q_i])
#     zero_count = 0
#     q_count = 0
#     total_zero = q_perms[perm_i].count('0') + num.count('0')
#     for i in range(len(num)):
#         if temp_num[i] == '0':
#             if i != zero_count:
#                 perm_count += i - zero_count
#             zero_count += 1

# print(perm_count % 1000000007)