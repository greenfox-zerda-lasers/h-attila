# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
# 
# Please remeber that negative amount of people would be troubling

# import view_elevator_template


class Elevator():


    def elevator_move(self, new_level, max_level):          # elevator mozgás lekezelése

        max_level -= 1

        if new_level < 0:
            return 0
        elif new_level >= max_level:
            return max_level
        else:
            return new_level

    def add_people(self, add_people, people_in_elevator, max_people_in_elevator):

        if add_people <= 0:
            add_people = 0

        new_people = people_in_elevator + add_people

        if new_people < 0:
            new_people = 0
        elif new_people > max_people_in_elevator:
            new_people = max_people_in_elevator

        return new_people


    def remove_people(self, remove_people, people_in_elevator):

        if remove_people < 0:
            remove_people = 0

        new_people = people_in_elevator - remove_people

        if new_people < 0:
            new_people = 0

        return new_people