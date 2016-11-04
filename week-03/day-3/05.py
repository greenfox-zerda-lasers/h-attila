# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods


class Stack():

    stack_list = []

    def size(self):
        return len(self.stack_list)

    def push(self, add_item):
        self.add_item = add_item
        self.stack_list.append(self.add_item)

    def pop(self):
        last_item = self.stack_list[-1]
        self.stack_list = self.stack_list[:-1]
        return last_item


kuka = Stack()
print(kuka.size())
kuka.push(1)
kuka.push(2)
kuka.push(3)
kuka.push(4)
kuka.push(5)
kuka.push(50)
kuka.push(99)
print(kuka.size())
print(kuka.pop())
print(kuka.stack_list)

