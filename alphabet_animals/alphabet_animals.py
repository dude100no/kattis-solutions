p1 = input()
last = p1[-1]

firstl_list = [False for i in range(26)]
word_list = []
a = ord('a')

for i in range(int(input())):
    w = input()
    l = w[0]
    firstl_list[ord(l) - a] = True
    if l == last:
        word_list.append(w)

found = False

if len(word_list) == 0:
    print("?")
    found = True

if len(word_list) == 1:
    w = word_list[0]
    l = w[-1]
    if l == last:
        print(w + "!")
        found = True

if not found:
    for w in word_list:
        l = w[-1]
        if not firstl_list[ord(l) - a]:
            print(w + "!")
            found = True
            break

if not found:
    print(word_list[0])