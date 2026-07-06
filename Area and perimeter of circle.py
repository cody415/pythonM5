# Beginner-friendly Circle class program without math library

class Circle:
    def __init__(self, radius):
        # Instance variable
        self.radius = radius

    def area(self):
        # Formula: π * r^2 (using 3.14 for π)
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        # Formula: 2 * π * r (using 3.14 for π)
        return 2 * 3.14 * self.radius


# Create Circle objects
circle1 = Circle(5)
circle2 = Circle(10)

# Display details
print("Circle 1:")
print("Radius:", circle1.radius)
print("Area:", circle1.area())
print("Perimeter:", circle1.perimeter())
print("-" * 30)

print("Circle 2:")
print("Radius:", circle2.radius)
print("Area:", circle2.area())
print("Perimeter:", circle2.perimeter())
