def magic_numbers(numbers):
    result = ''
    return int(result.join(sorted(list(str(numbers)), reverse = True)))





szam = 12345534543534

print(magic_numbers(szam))