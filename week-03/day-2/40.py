students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

def candi(input):
        list_of_students = []
        owned_candies = 0
        print("*** A diakok listaja ***")
        for i in input:
                list_of_students = i
                print("nev:", list_of_students['name'], "eletkor: ", list_of_students['age'], "cukorkak: ", list_of_students['candies'])
                if list_of_students['age'] < 10:
                        owned_candies += list_of_students['candies']
        print("cukorkak szama 10 ev alatt:", owned_candies)

candi(students)

