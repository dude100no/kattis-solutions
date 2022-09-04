min_size = int(input(""))
input_no_size = list(map(int, input("").split(" ")))
# no_size = [int(e) for e in input_no_size]

# min_no_size = [2 ** (i + 1) for i in range(len(no_size))]
# print(min_no_size)
# print(no_size)

#constant variables



#to obtain the dimensions the sizes of paper
def paper_dim(h, w, size):
    if size == 2:
        return h, w
    w /= 2
    return paper_dim(w, h, size - 1)

a0_h = 2 ** (-3/4)
a0_w = 2 ** (-5/4)



#to find out the combination of sizes of papers to fit together that uses the least pieces of paper
max_no = 2 ** (min_size - 1)
# print(max_no)
count = 0
done = False
new_no_size = []
for i, e in enumerate(new_no_size):
    if e == 0:
        continue
    for paper in range(e):
        count += 2 ** (min_size - i - 2)
        if count == max_no:
            done = True
            break
    new_no_size.append([i + 2, paper + 1])
    if done:
        break
print(new_no_size)

#finding minimum length required
if not done:
    print("impossible")
else:
    new_min_size = new_no_size[-1][0]
    new_max_no = 2 ** (new_min_size - 1)
    if new_min_size % 2 == 0:
        h, w = paper_dim(new_min_size)
        total_len = ((new_max_no ** 0.5) - 1) * (h + w) * (new_max_no ** 0.5)
        for size, num in new_no_size:
            # h, w = paper_dim(size)
            if size % 2 == 1:
                var_no = 2 ** (new_min_size - size)
                total_len -= ((var_no ** 0.5) - 1) * (h + w) * (var_no ** 0.5)
            else:
                var_no = 2 ** (new_min_size - size - 1)
                total_len -= (2 * (((var_no ** 0.5) - 1) * (h + w) * (var_no ** 0.5)) + paper_dim(size + 1)[0])
    else:
        h, w = paper_dim(new_min_size)
        total_len = ((max_no ** 0.5) - 1) * (h + w) * (max_no ** 0.5)
        for size, num in new_no_size:
            # h, w = paper_dim(size)
            if size % 2 == 0:
                var_no = 2 ** (min_size - size)
                total_len -= ((var_no ** 0.5) - 1) * (h + w) * (var_no ** 0.5)
            else:
                var_no = 2 ** (min_size - size - 1)
                total_len -= (2 * (((var_no ** 0.5) - 1) * (h + w) * (var_no ** 0.5)) + paper_dim(size + 1)[0])




    print(total_len)