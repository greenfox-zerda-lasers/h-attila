# Model file for _todo_ app

import todo_texts_template
import csv


class TodoModel():


    def add_item(self, new_item, data_file_name):

        self.todo_data = self.data_read_from_file(data_file_name)
        self.todo_data.append(str(new_item) + ';\n')
        self.data_write_to_file(self.todo_data, data_file_name)



    def remove_item(self, item_number, data_file_name):

        self.todo_data = self.data_read_from_file(data_file_name)
        self.todo_data.remove(self.todo_data[item_number-1])
        self.data_write_to_file(self.todo_data, data_file_name)


    def check_item(self, item_number, data_file_name):

        self.todo_data = self.data_read_from_file(data_file_name)
        print(self.todo_data)



    def data_read_from_file(self, data_file_name):

        todo_file = open(data_file_name, "w")
        todo_data = todo_file.readlines()
        todo_file.close()


        return todo_data


    def data_write_to_file(self, todo_data, data_file_name):

        self.todo_data = todo_data

        try:
            todo_file_write = open(data_file_name, "w")
            for i in self.todo_data:
                todo_file_write.write(i)
            todo_file_write.close()

        except:
            print(todo_texts_template.data_file_unknown_write_error)