# Creating our Calculator class
class Calculator:

    def __init__(self):
        print("Welcome to the Calculator")

    # Creating a function that will add two arguments
    def add(self, num1, num2):
        return num1 + num2

    # Creating a function that will subtract two arguments
    def subtract(self, num1, num2):
        return num1 - num2  #

    # Create a function to multiply (*)
    def multiply(self, num1, num2):
        return num1 * num2

    # Create a function to do division (/)
    def divide(self, num1, num2):
        if num2 == 0:  # We shouldn't allow division by 0 so let's check for that
            return "Please don't try and divide by zero"
        else:
            return num1 / num2

    # Create a function to do modulo division (%)
    def modulo(self, num1, num2):
        if num2 == 0:  # We shouldn't allow division by 0 so let's check for that
            return "Please don't try and divide by zero"
        else:
            return num1 % num2

    # Create a function to do exponentials (^)
    def exponent(self, num1, num2):
        result = num1  # Creating the variable we wish to print
        for _ in range(num2 - 1):  # This loop will run for the amount of times stored in the num2 variable
            result = result * num1  # Multiplies the current value of the calculation with its original value
        return result  # Printing the final result

    # Create a function to check if one number is cleanly divisible by the other
    def is_divisible(self, num1, num2):
        if self.modulo(num1, num2) == 0:
            return True
        else:
            return False

    # Create a function to calculate the area of a triangle when given its base and height
    def area_of_triangle(self, base, height):
        return base * height * 0.5

    # Create a function to convert a provided value in inches to cm
    def inch_to_cm(self, num_of_inches):
        return self.multiply(num_of_inches, 2.54)


# Creating an object of our Calculator class and testing that the output for the class methods is correct
calc = Calculator()
print(calc.add(7, 9))
print(calc.subtract(8, 54))
print(calc.multiply(4, 16))
print(calc.divide(80, 0))
print(calc.divide(80, 5))
print(calc.modulo(90, 8))
print(calc.modulo(70, 0))
print(calc.exponent(5, 4))
print(calc.is_divisible(10, 3))
print(calc.area_of_triangle(5, 8))
print(calc.inch_to_cm(5))
