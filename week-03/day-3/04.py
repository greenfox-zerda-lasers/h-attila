# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades


class Student():

    grade = 0
    average = 0
    grades = []

    def __init__(self, student_name):
        self.student_name = student_name

    def add_grade(self, grade):
        self.grade = grade
        if self.grade > 5 and self.grade < 1:
            print("Érvénytelen osztályzat!")
        else:
            self.grades.append(self.grade)
            print(self.grades)

    def get_average(self):
        self.average = sum(self.grades) / len(self.grades)
        return int(self.average)

Pistike = Student("Pistike")
Pistike.add_grade(1)
Pistike.add_grade(2)
Pistike.add_grade(5)
print(Pistike.get_average())