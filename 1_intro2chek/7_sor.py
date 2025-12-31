# from pwn import xor

def manual_xor(string, number):
  res = ""
  for char in string:
    order = ord(char) ^ number
    res += chr(order)
  return res

label = "label"

res = manual_xor(label, 13)

# res = xor(label, 13)

print(res)