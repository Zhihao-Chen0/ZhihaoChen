class Shape:
    def draw(self):
        raise NotImplementedError("You should implement this method.")

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        if shape_type == "triangle":
            return Triangle()
        else:
            return None


factory = ShapeFactory()
try:
    shape = factory.create_shape("circle")
    print(shape.draw())
except AttributeError:
    print("Invalid shape type provided.")
try:
    shape = factory.create_shape("square")
    print(shape.draw())
except AttributeError:
    print("Invalid shape type provided.")
try:
    shape = factory.create_shape("triangle")
    print(shape.draw())
except AttributeError:
    print("Invalid shape type provided.")
