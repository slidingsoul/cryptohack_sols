# this is a naive solution
# you see, there are three choices of a_square which are 14, 6, and 11
# you can check whether 14, and 11 has a solution by checking 6^((29-1)/2)
# is congruent to 1

p = 29
a_square = 6
for i in range (1, p):
  if ((i ** 2 % p) == a_square):
    print(i)