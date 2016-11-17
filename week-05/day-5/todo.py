import sys
import todo_texts
import os



class MainLoop():

    def __init__(self):

        os.system('cls' if os.name == 'nt' else 'clear')

#        print(sys.argv, len(sys.argv))

        if len(sys.argv) > 1:                                   # ha van megadva kapcsoló a program híváskor
            if sys.argv[1] == '-l':                             # LIST elements
                ListItems()


            if sys.argv[1] == '-a':                             # ADD element
                print('ADD elements')
                FileHandling.data_read_from_file(self)

            if sys.argv[1] == '-r':                             # REMOVE element
                print('REMOVE elements')

            else:
                pass                                            # invalid input, error handling
        else:
            MainScreen()


class MainScreen():

    def __init__(self):
        print(todo_texts.main_menu)                             # no attributum added


class ListItems():

    def __init__(self):

        FileHandling.data_read_from_file(self)
        print(todo_texts.list_items_header)
        for i in range(len(self.todo_data)):
            item = str(self.todo_data[i]).rstrip().split(';')
            print(' {} - [{}] {}'.format(i + 1, item[1], item[0]))
        print('\n')


class AddItem():
    pass


class RemoveItem():
    pass


class FileHandling():

    def data_read_from_file(self):
        try:

            self.data_file_name = 'todo_data.csv'

            todo_file = open(self.data_file_name, "r")
            self.todo_data = todo_file.readlines()
            todo_file.close()

        except FileNotFoundError:
            open(self.data_file_name, "w")
            print(todo_texts.data_file_not_found)
            self.todo_data = []

        except:
            print(todo_texts.data_file_unknown_read_error)
            self.todo_data = []

        return self.todo_data


    def data_write_to_file(self, todo_data):
        try:
            todo_file = open(self.data_file_name, "w")
            todo_file.write(self.todo_data)
            todo_file.close()

        except:
            print(todo_texts.data_file_unknown_write_error)


################  MAIN LOOP  ################


todo_app = MainLoop()


