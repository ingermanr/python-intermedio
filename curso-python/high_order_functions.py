# filter

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

odd = [i for i in my_list if i % 2 != 0]

print(odd)

other_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

odd = list(filter(lambda x: x % 2 != 0, other_list))

print(odd)

# map

third_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

sqrs = [i**2 for i in third_list]

print(sqrs)

sqrs_map = list(map(lambda x: x**2, third_list))

print(sqrs_map)

# reduce

from functools import reduce

fourt_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

all_mult = reduce(lambda a,b: a*b, my_list)

print(all_mult)
