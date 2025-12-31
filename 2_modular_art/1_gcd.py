def find_gcd(a, b):
  if (a == b):
    return a
  while b > 0:
    r = a % b
    a = b
    b = r
  return a

def rec_find_gcd(a, b):
  if (a == b) or b == 0:
    return a
  return rec_find_gcd(b, a % b)

print(find_gcd(10, 45))
print(find_gcd(3768, 1701))
print(find_gcd(31, 2))

print(rec_find_gcd(10, 45))
print(rec_find_gcd(66528, 52920))
