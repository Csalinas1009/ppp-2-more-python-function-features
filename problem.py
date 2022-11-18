def max_num(a, b, c):
    return max([a, b, c])


print(max_num(1, 2, 3))
print(max_num(100, 200, 300))
print(max_num(10000, 4, 260000))


def multi_list(lst):

    if len(lst) == 0:
        return 0

    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i
        return prod


print(multi_list([1, 3, 4]))
print(multi_list([14, 22, 9]))
print(multi_list([100, 14, 99]))


def rev_string(my_str):
    return my_str[::-1]


print(rev_string("boop"))
print(rev_string("string"))
print(rev_string("recursion"))


def num_within(x, a, b):
    return x in range(a, b+1)


print(num_within(2, 4, 5))
print(num_within(3, 2, 4))
print(num_within(10, 20, 30))
