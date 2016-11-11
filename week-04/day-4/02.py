# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def magic_addon(n):

    if n <= 1:
        return 1
    else:
        return n + magic_addon(n-1)


print(magic_addon(3))