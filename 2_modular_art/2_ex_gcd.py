def find_egcd(a, b):
  if (b == 0):
    return a, 1, 0
  # first row
  q = a // b
  r = a % b
  s1 = 1
  s2 = 0
  s3 = 1
  t1 = 0
  t2 = 1
  t3 = t1 - (q * t2)
  while r > 0:
    a = b
    b = r
    q = a // b
    r = a % b
    # shifting only
    s1 = s2
    s2 = s3
    t1 = t2
    t2 = t3
    # formulating
    s3 = s1 - (q * s2)
    t3 = t1 - (q * t2)

  return b, s2, t2

# use default arguments
def rec_find_egcd(a, b, s1 = 1, s2 = 0, t1 = 0, t2 = 1):
  if (b == 0):
    return a, 1, 0
  q = a // b
  r = a % b
  s3 = s1 - (q * s2)
  t3 = t1 - (q * t2)

  if (r == 0):
    return b, s2, t2
  else:
    return rec_find_egcd(b, r, s2, s3, t2, t3)

p=26513
q=32321
print(rec_find_egcd(161, 28))

print(rec_find_egcd(p, q))