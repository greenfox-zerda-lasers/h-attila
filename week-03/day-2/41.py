students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

# create a function that counts the students that
# has more than 4 candies

def candies_of_students(input_data):
    number_of_candies = 0
    print(" *** 4 cukorka feletti gyermekek ***")
    for i in input_data:
        if i['candies'] > 4:
            number_of_candies += i['candies']
            print("nev:", i['name'] + ", number of candies:", i['candies'])
    print("sum of candies:", number_of_candies)


candies_of_students(students)


