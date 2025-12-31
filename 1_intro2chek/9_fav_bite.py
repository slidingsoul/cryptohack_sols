from pwn import xor

enc = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")


for i in range(0, 256): 
  try:
    res = xor(enc, i).decode()
    if "crypto" in res:
      print(res)
      print(i)
      break
  except UnicodeDecodeError:
    print(UnicodeDecodeError)