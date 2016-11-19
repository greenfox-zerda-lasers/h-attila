import csv

my_data = []

with open('todo_data.csv', newline='') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=';', quotechar='|')
    for line in csv_data:
#        print(line)
        my_data.append(line)

    print(my_data[2])