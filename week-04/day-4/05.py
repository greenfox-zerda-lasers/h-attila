# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def magic_bunnies(number, ears):

    if number <= 1:
        return ears
    else:
        return ears + magic_bunnies(number-1, ears)

print(magic_bunnies(17,5))