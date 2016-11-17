class Shape:
	def __init__(self,color="black"):
		self.color = color

	def getArea(self):
		raise TypeError

	def draw(self):
		print("I'm here :)")

	def toString(self):
		pass

class Rectangle(Shape):
	def __init__(self, a, b):
		super().__init__()
		self.a = a
		self.b = b

	def getColor(self):
		print(self.color)

	def getArea(self):
		return self.a * self.b

class App:
	def createShape(self):
		self.shapes = []
		for x in range(10):
			rect = Rectangle(10, 20)
			self.shapes.append(rect)

	def update(self):
		for shape in self.shapes:
			shape.draw()

myapp = App()
myapp.createShape()
myapp.update()