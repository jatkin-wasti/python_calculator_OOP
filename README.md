# Task
## Build a Calculator using Classes
### Phase 1
- Build a simple calculator class containing add, subtract, multiply, and divide
### Phase 2 - Expand by creating
- Divisible by method that returns ```True``` or ```False``` depending on the outcome
- Work out and return the area of a triangle
- Create an inch to cm converter
## Solution
### Creating our class
- First we create the class, we don't have any class variables to set so let's just print a message 
when initialised
```
class Calculator:

    def __init__(self):
        print("Welcome to the Calculator")
``` 
### Creating methods to perform our calculator functions
- First for addition we create a simple method
```
    def add(self, num1, num2):
        return num1 + num2
```
- Then another for subtraction
```
    def subtract(self, num1, num2):
        return num1 - num2  #
```
- Then one for multiplication
```
    def multiply(self, num1, num2):
        return num1 * num2
```
- Then one for division, but this one is slightly more complex
```
    def divide(self, num1, num2):
        return num1 / num2
```
- But wait! If the user provides a 0 as num2, the code will break!
- Let's perform a simple check to see if num2 is 0 and output a warning to the user
```
    def divide(self, num1, num2):
        if num2 == 0:  # We shouldn't allow division by 0 so let's check for that
            return "Please don't try and divide by zero"
        else:
            return num1 / num2
```
- We'll have to do the same for modulo as well
```
    def modulo(self, num1, num2):
        if num2 == 0:  # We shouldn't allow division by 0 so let's check for that
            return "Please don't try and divide by zero"
        else:
            return num1 % num2
```
- Now onto a more complex operation, exponentials!
- We need to accept two arguments and multiply the first number with itself for as many times as is stated in the second
number
- A loop sounds good but we can't just use the number provided as both values in the multiplication within the loop 
because this number will get bigger each iteration
- To get around this, we'll create a variable that will change throughout execution, and one that keeps the original
 value
```
    def exponent(self, num1, num2):
        result = num1  # Creating the variable we wish to print
        for _ in range(num2 - 1):  # This loop will run for the amount of times stored in the num2 variable
            result = result * num1  # Multiplies the current value of the calculation with its original value
        return result  # Printing the final result
```
- Phew! Now we need to add a method that checks if one number is divisible by another
- This is easily achieved by calling our modulo method and checking if the returned result is 0, because if there is no
 remainder it must be cleanly divisible
```
    def is_divisible(self, num1, num2):
        if self.modulo(num1, num2) == 0:
            return True
        else:
            return False
```
- Then we need a method that calculates the area of a triangle, which is simply 1/2 multiplied by the base and height
```
    def area_of_triangle(self, base, height):
        return base * height * 0.5
```
- Finally, we just need to add a converter from inches into cm
- 1 inch is 2.54 centimetres so we can just call the multiply function with the number of inches and 2.54 to do our 
conversion
```
    def inch_to_cm(self, num_of_inches):
        return self.multiply(num_of_inches, 2.54)
```
- Now that our class is complete, let's test it by creating an instance and running our methods
```
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
```
- These all return the correct values so we know that our class works as intended