# 47__super_function
# class Rectange:
#     pass
#
# class Square(Rectange):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
# class Cube(Rectange):
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height


# annat sätt som effektivare kan skriva
class Rectange:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectange):
    def __init__(self, length, width):
        super().__init__(length, width) # import från parents

    def area(self):
        return self.length*self.width

class Cube(Rectange):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height # detta är skillnaden alltså difference in the code

    def volym(self):
        return self.length * self.width * self.height

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volym())