# Create a class the displays the Elevator art and navigation (list of commands)

import os
import view_elevator_template


class Drawing_module():                                       # Building MAIN functions


    def draw_building(self, data):                            # data = max_building_level, elevator_level, people_in_elevator

        self.data = data

        os.system('cls' if os.name == 'nt' else 'clear')

        print(view_elevator_template.building_roof.format(self.data["elevator_level"], self.data["people_in_elevator"], self.data["max_people_in_elevator"]))

        if self.data["elevator_level"] == 0:
            for i in range(self.data["max_building_level"] - self.data["elevator_level"]-1):
                print(view_elevator_template.building_body_without_elevator)
            print(view_elevator_template.building_ground_with_lift.format(self.people_in_elevator()))

        else:
            for i in range(self.data["max_building_level"] - self.data["elevator_level"]-1):
                print(view_elevator_template.building_body_without_elevator)
            print(view_elevator_template.building_body_with_elevator.format(self.people_in_elevator()))
            for j in range(self.data["elevator_level"]-1):
                print(view_elevator_template.building_body_without_elevator)

            print(view_elevator_template.building_ground_without_lift)



    def people_in_elevator(self):

        if self.data["people_in_elevator"] == 0:
            return view_elevator_template.elevator_empty
        elif self.data["people_in_elevator"] == 1 :
            return view_elevator_template.elevator_1
        elif self.data["people_in_elevator"] == 2:
            return view_elevator_template.elevator_2
        elif self.data["people_in_elevator"] == 3:
            return view_elevator_template.elevator_3
        elif self.data["people_in_elevator"] == self.data["max_people_in_elevator"]:
            return view_elevator_template.elevator_full
        else:
            return view_elevator_template.elevator_more.format(self.data["people_in_elevator"])
