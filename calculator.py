
class Calculator:

    def __init__(self):
        print("Welcome to the Calculator")

    # Creating a function that will add two arguments
    def add(self, num1, num2):  # Takes two arguments
        print(num1 + num2)  # Print the result

    # Creating a function that will subtract two arguments
    def subtract(self, num1, num2):  # Defining the function with two arguments
        print(num1 - num2)  # Printing the value of one subtracted by the other

    # Create a function to multiply (*)
    def multiply(self, num1, num2):
        return num1 * num2

    # Create a function to do division (/)
    def divide(self, num1, num2):
        return num1 / num2

    # Create a function to do modulo division (%)
    def modulo(self, num1, num2):
        return num1 % num2

    # Create a function to do exponentials (^)
    def exponent(self, num1, num2):
        result = num1  # Creating the variable we wish to print
        for _ in range(num2 - 1):  # This loop will run for the amount of times stored in the num2 variable
            result = result * num1  # Multiplies the current value of the calculation with its original value
        return result  # Printing the final result
