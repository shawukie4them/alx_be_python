from polymorphism_demo import Rectangle, Circle

def run_tests():
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    print(f"The area of the Rectangle is: {rectangle.area()}")
    print(f"The area of the Circle is: {circle.area()}")

if __name__ == "__main__":
    run_tests()