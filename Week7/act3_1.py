class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"
    
# It should raise an error because Triangle class is not defined

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        else:
            return None


factory = ShapeFactory()
shape = factory.create_shape("triangle")   
print(shape.draw())  
# This will raise an AttributeError since shape is None
