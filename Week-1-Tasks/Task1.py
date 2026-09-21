import math


def calculate_area_Of_circle(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    radius = float(input("Enter the radius of the circle: "))
    print(f"The area of the circle with radius {radius} is: {calculate_area_Of_circle(radius):.2f}")