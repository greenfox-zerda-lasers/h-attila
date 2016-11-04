# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well


class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(self.first_name, self.last_name)

class Student(Person):

    grades = []
    grade = 0

    def add_grades(self, grade):
        self.grade = grade
        self.grades.append(self.grade)


    def salute(self):
        self.greet()
        print(sum(self.grades)/len(self.grades))


bela = Person("Ló", "Béla")
bela.greet()

geza = Student("Kiss", "Geza")
geza.greet()
geza.add_grades(1)
geza.add_grades(5)
geza.salute()
