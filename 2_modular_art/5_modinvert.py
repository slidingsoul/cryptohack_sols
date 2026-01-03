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
  
a = 13 # mod
b = 3 # d
print(rec_find_egcd(a, b))
x, y, z = rec_find_egcd(a, b)
res = a + z
print(res)