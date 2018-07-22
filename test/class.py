class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def slide_y_axis(self,amt):
        self.y += amt;

p = Point(3, 5, -2)
print(p.x)
print(p.y)
print(p.z)
p.slide_y_axis(-5)
print(p.y)
