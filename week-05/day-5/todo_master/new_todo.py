# Controller file for _ToDo_

import sys
import todo_texts_template
import todo_model
import todo_view


class Controller():

    def __init__(self):

        self.data_file_name = 'todo_data.csv'
        self.todo_data = []

    def list_items(self):

        todo_data = ToDo_Model.data_read_from_file(self.data_file_name)
        print(todo_data)
        ToDo_View.print_todo_list(todo_data)

    def add_item(self):

        ToDo_Model.add_item("".join(sys.argv[2:]), self.data_file_name)

    def remove_item(self):

        ToDo_Model.remove_item(int(sys.argv[2]), self.data_file_name)

    def check_item(self):

        ToDo_Model.check_item(int(sys.argv[2]), self.data_file_name)


############ Main Loop starts here ############


ToDo_Controller = Controller()
ToDo_Model = todo_model.TodoModel()
ToDo_View = todo_view.TodoView()

print(sys.argv, len(sys.argv))

is_running = True

while is_running:

if len(sys.argv) > 1:
    if sys.argv[1] == '-l':
        ToDo_Controller.list_items()

    elif sys.argv[1] == '-a':
        print('ADD elements')
        ToDo_Controller.add_item()

    elif sys.argv[1] == '-r':
        print('REMOVE elements')
        ToDo_Controller.remove_item()

    elif sys.argv[1] == '-c':
        print('CHECK element')
        ToDo_Controller.check_item()

    else:
        ToDo_View.print_menu()

else:
    ToDo_View.print_menu()