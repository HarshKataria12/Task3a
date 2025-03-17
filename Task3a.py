from math import sqrt
# Base class: Shape with multiple sides
class Polygon:
    def __init__(self, sides):
        self.sides = sides  # Store side lengths as a list
    def is_valid(self):
        """Verify if the shape qualifies as a polygon."""
        return len(self.sides) >= 3
    def perimeter(self):
        """Compute the sum of all side lengths."""
        return sum(self.sides)

# Subclass: Four-sided polygon
class Quadrilateral(Polygon):
    def __init__(self, side1, side2, side3, side4):
        super().__init__([side1, side2, side3, side4])
    
    def is_valid(self):
        """Ensure it has exactly four sides."""
        return len(self.sides) == 4

# Subclass: Rectangular shape
class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)
    
    def area(self):
        """Calculate the rectangle's area."""
        return self.sides[0] * self.sides[1]

# Subclass: Square (special rectangle)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Subclass: Parallelogram with optional height
class Parallelogram(Quadrilateral):
    def __init__(self, base, side, height=None):
        super().__init__(base, side, base, side)
        self.height = height
    
    def area(self):
        """Find the area if height is given."""
        if self.height is not None:
            return self.sides[0] * self.height
        raise ValueError("Height must be provided to compute the area.")

# Subclass: Rhombus with optional diagonals
class Rhombus(Quadrilateral):
    def __init__(self, side, diagonal1=None, diagonal2=None):
        super().__init__(side, side, side, side)  # Equal sides for rhombus
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    
    def area(self):
        """Compute area using diagonals if available."""
        if self.diagonal1 and self.diagonal2:
            return (self.diagonal1 * self.diagonal2) / 2
        raise ValueError("Both diagonals are required for area calculation.")
