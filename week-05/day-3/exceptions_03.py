# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Big_mistake(Exception):
    print('[ *** Nagyon - nagyon - nagyon - nagyon - nagy hiba! *** ]')



class Person():

    def name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def birthdate(self, birth_date):
        self.birth_date = birth_date.split('.')
        self.birth_year = int(self.birth_date[0])
        self.birth_month = int(self.birth_date[1])
        self.birth_day = int(self.birth_date[2])

        if self.birth_year < 0 or 2016 < self.birth_year:
            raise Big_mistake

    def greetings(self):
        return "Hi! Your full name {}, and your birthdate is {} year, {} month, {} day." .format(self.first_name + " " + self.last_name, self.birth_year, self.birth_month, self.birth_day)


jozsi = Person()
jozsi.name("John", "Smith")
try:
    jozsi.birthdate('2017.04.05')
except Big_mistake:
    pass

print(jozsi.greetings())