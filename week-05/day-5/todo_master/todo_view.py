# View file for _todo_ app

import os
import todo_texts_template

class TodoView():

    def print_todo_list(self, todo_data):
        print(todo_texts_template.list_items_header)

        for i in range(len(todo_data)):
            item = str(todo_data[i]).rstrip('\n').split(';')
            if item[1] == "":
                item[1] = " "
            print(' {} - [{}] {}'.format(i + 1, item[1], item[0]))
        print('\n')


#        os.system('cls' if os.name == 'nt' else 'clear')

    def print_menu(self):
        print(todo_texts_template.main_menu)