input_min_size = int(input(""))
input_no_size = list(map(int, input("").split(" ")))

paper_no_arr = []

# to find the number of smallest sized paper need to fit in the respective paper sizes
def num_min_size_function(size, min_size):
    return 2 ** (min_size - size)

# to find the height and widith of the respective sizes of paper
def paper_dim(h, w, size):
    if size == 1:
        return h, w
    w /= 2
    return paper_dim(w, h, size - 1)

# the total length of tape if made out of only minimum sized paper for the respective paper sizes
def min_size_for_paper(size_h, size_w, min_h, min_w):
    total_tape_size = size_h * ((size_h / min_h) - 1) + size_w * ((size_w / min_w) - 1)
    return total_tape_size


num_min_size_a1 = num_min_size_function(1, input_min_size)
total_num = 0
for index in range(len(input_no_size)):
    paper_no_arr.append(input_no_size[index])
    if input_no_size[index] == 0:
        continue
    total_num += num_min_size_function(index + 2, input_min_size) * input_no_size[index]
    possibility = "impossible"
    if total_num >= num_min_size_a1:
        possibility = "possible"
        break

min_size = len(paper_no_arr) + 1

if possibility == "possible":
    a1_h = 2 ** (-3/4)
    a1_w = 2 ** (-1/4)

    # min size paper dimensions
    min_h, min_w = paper_dim(a1_h, a1_w, min_size)

    total_tape = min_size_for_paper(a1_h, a1_w, min_h, min_w)


    for index in range(len(paper_no_arr)):
        if paper_no_arr[index] == 0:
            continue
        total_tape -= min_size_for_paper(paper_dim(a1_h, a1_w, index+2)[0], paper_dim(a1_h, a1_w, index+2)[1], min_h, min_w) * paper_no_arr[index]

    print(total_tape)
elif possibility == "impossible":
    print(possibility)