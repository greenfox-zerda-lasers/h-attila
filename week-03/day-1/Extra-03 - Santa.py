data = [line.strip() for line in open("extra_03.txt", 'r')]

print(data)

for i in range(len(data)):
    print(data[i])
    sz, h, m = data[i].split('x')
    print("Sz, h, m: ", sz, h, m)