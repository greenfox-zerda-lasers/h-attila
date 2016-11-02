j1 = 10
j2 = 3
# tell if j1 is higher than j2 squared and smaller than j2 cubed
print("j2 squared:", j2 ** 2)
print("j2 cubed:", j2 ** 3)
if (j1 > (j2 ** 2)) and ((j1 < j2) ^ 3):
    print("ok!")
else:
    print("not ok")
