Task 3:
a) Design and implement a hierarchy of classes of polygons (in a language of your choice) based on the following
information:
i. a polygon class
ii. classes: quadrilateral, square, rectangle, parallelogram, and rhombus

Test Case:
def test_polygon():
    p = Polygon([3, 4, 5])
    print("Polygon Valid:", p.is_valid())  # Expected: True
    print("Polygon Perimeter:", p.perimeter())  # Expected: 12

def test_quadrilateral():
    q = Quadrilateral(2, 3, 4, 5)
    print("Quadrilateral Valid:", q.is_valid())  # Expected: True
    print("Quadrilateral Perimeter:", q.perimeter())  # Expected: 14

def test_rectangle():
    r = Rectangle(4, 5)
    print("Rectangle Area:", r.area())  # Expected: 20
    print("Rectangle Perimeter:", r.perimeter())  # Expected: 18

def test_square():
    s = Square(4)
    print("Square Area:", s.area())  # Expected: 16
    print("Square Perimeter:", s.perimeter())  # Expected: 16

def test_parallelogram():
    p = Parallelogram(5, 7, height=4)
    print("Parallelogram Area:", p.area())  # Expected: 20
    print("Parallelogram Perimeter:", p.perimeter())  # Expected: 24

def test_parallelogram_missing_height():
    p = Parallelogram(5, 7)
    try:
        print("Parallelogram Area:", p.area())  # Should raise ValueError
    except ValueError as e:
        print("Parallelogram Error:", e)  # Expected: "Height is required to calculate area."

def test_rhombus():
    r = Rhombus(6, diagonal1=8, diagonal2=10)
    print("Rhombus Area:", r.area())  # Expected: 40
    print("Rhombus Perimeter:", r.perimeter())  # Expected: 24

def test_rhombus_missing_diagonals():
    r = Rhombus(6)
    try:
        print("Rhombus Area:", r.area())  # Should raise ValueError
    except ValueError as e:
        print("Rhombus Error:", e)  # Expected: "Both diagonals are required to calculate area."

# Run all tests
test_polygon()
test_quadrilateral()
test_rectangle()
test_square()
test_parallelogram()
test_parallelogram_missing_height()
test_rhombus()
test_rhombus_missing_diagonals()
