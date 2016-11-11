# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


def magic_counter(n):

    if n <= 1:
        return 1

    else:
        return n % 10 + magic_counter(n // 10)


print(magic_counter(1234))
