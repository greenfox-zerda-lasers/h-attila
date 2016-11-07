from operator import itemgetter

key = 0
value = ''

d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
for key, value in sorted(d.items(), itemgetter(1), True):
    print(key, value)