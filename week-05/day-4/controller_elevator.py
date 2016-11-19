# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

import view_elevator
import view_elevator_template
import model_elevator
import time


class Controller():

    def __init__(self):                         # main data for commucation

        self.building_data = {
            "max_building_level" : 10,
            "elevator_level" : 0,
            "people_in_elevator" : 0,
            "max_people_in_elevator" : 6
        }


    def main_menu(self):                        # show main menu and waiting for input

        print(view_elevator_template.main_menu)
        return input(view_elevator_template.user_input)


    def elevator_move(self):                    # move the elevator

        old_level = self.building_data["elevator_level"]
        try:
            new_level = int(input(view_elevator_template.new_level_input))
        except ValueError:
            new_level = 0
        self.building_data["elevator_level"] = Elevator_Model.elevator_move(new_level, self.building_data["max_building_level"])

        if old_level - self.building_data["elevator_level"] > 1:                        # move down
            for i in range(old_level, self.building_data["elevator_level"], -1):
                self.building_data["elevator_level"] = i-1
                Elevator_View.draw_building(self.building_data)
                time.sleep(0.3)

        elif old_level-self.building_data["elevator_level"] < 1:                        # move up
            for i in range(old_level, self.building_data["elevator_level"], 1):
                self.building_data["elevator_level"] = i+1
                Elevator_View.draw_building(self.building_data)
                time.sleep(0.3)

    def elevator_add_people(self):

        try:
            add_people = int(input(view_elevator_template.add_people_input))
        except ValueError:
            add_people = 0
        self.building_data["people_in_elevator"] = Elevator_Model.add_people(add_people, self.building_data["people_in_elevator"], self.building_data["max_people_in_elevator"])

        Elevator_View.draw_building(self.building_data)


    def elevator_remove_people(self):
        try:
            remove_people = int(input(view_elevator_template.remove_people_input))
        except ValueError:
            remove_people = 0
        self.building_data["people_in_elevator"] = Elevator_Model.remove_people(remove_people, self.building_data["people_in_elevator"])

        Elevator_View.draw_building(self.building_data)



######## MAIN Loop starts here ########


Elevator_Controller = Controller()
Elevator_View = view_elevator.Drawing_module()
Elevator_Model = model_elevator.Elevator()

is_running = True

while is_running:

    Elevator_View.draw_building(Elevator_Controller.building_data)          # refresh elevator drawing
    menu_item = Elevator_Controller.main_menu()                             # get user input

    if menu_item == "move":
        Elevator_Controller.elevator_move()

    elif menu_item == "add":
        Elevator_Controller.elevator_add_people()

    elif menu_item == "remove":
        Elevator_Controller.elevator_remove_people()

    elif menu_item == "exit":
        is_running = False