# import library
import math

# circle area
circle_radius = float(input("Enter the circle radius: "))
circle_area = math.pi * circle_radius ** 2
print(f"The circle area is: {circle_area}")

# date
date = input("Enter the date: ").split("/")
print(f"Day: {date[0]}, Month: {date[1]}, Year: {date[2]}")

# example of type error
try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(f"The division of the numbers is: {n1 / n2}")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except Exception as e:
    print(f"An error occurred: {e}")

print("End of program")