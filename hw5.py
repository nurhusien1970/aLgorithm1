

# 1

AList = [1, 8, 6, 2, 9, 7, 4]


def split(l):
    odd = []
    even = []
    count_odd = 0
    count_even = 0
    for i in l:
        if (i % 2) == 0:
            even.append(i)
            print('even in list ', even)
            count_even += 1
            print('and count even in list is', count_even)
        else:
            odd.append(i)
            count_odd += 1
            print('odd in list is ', odd, '\n and count in odd_list is ', count_odd)
    print('for loop even + odd ', even + odd, 'and count even and odd is ', count_odd, count_even)


split(AList)

AList = [1, 8, 7, 4]

odd_only = [num for num in AList if num % 2 == 1]
print(odd_only)
even_only = [num for num in AList if num % 2 == 0]
print(even_only + odd_only)

odd, even = [], []
num = 0

while num < len(AList):
    if AList[num] % 2 == 0:
        even.append(AList[num])
    else:
        odd.append(AList[num])
    num += 1
print(odd, even, even + odd)

# using filter

even = list(filter(lambda x: (x % 2 == 0), AList))
odd = list(filter(lambda x: x % 2 == 1, AList))
print(even + odd)

# 2
L = [8, 9, 8, 9, 9]
L_new = list(set(L))
print(L_new)

if len(L_new) == 1:
    # L = np.array(L)
    L_new2 = [0] * len(L)
    print("len", len(L))
    L_new2.insert(0, 1)
    print("L_new2", L_new2)

count2 = 0

if L[0] == 9:
    count2 += 1

for i in range((len(L) - 1), 0, -1):
    print(i)
    if L[i] == 9 and L[i - 1] == 9:
        print("Li", L[i], "Li", L[i - 1])

        count2 += 1

    if L[i] == 9 and L[i - 1] != 9:
        count2 += 1
        break
print("count2is ", count2)

L1 = [0] * count2
b = len(L) - count2
L = L[0:b] + L1
print("first", L)
L[b - 1] = L[b - 1] + 1
# L2[-1]+ (L[-1]+1)

print("L", L)
