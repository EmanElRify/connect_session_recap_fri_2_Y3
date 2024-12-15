#Write a Python function called multiply_numbers that takes two arguments
# , num1 and num2. 
# Inside the function, calculate the product of these two numbers 
# and return the result.
def multiply_numbers(num1, num2):
    # global x
    # x = num1 * num2
    if num1 == 1:
        return num1 * num2
    print("Thanks for using my calculator")
    
    

x = multiply_numbers(5,3)
print(x)

def add_numbers(a, b):
   return a + b

# Scenario 1: Function call
result = add_numbers(3, 4)
print(result)
# _______________________________
def multiply_numbers(x, y):
   return x * y

# Scenario 2: Function not called
print(multiply_numbers)
# ________________________________

def greet(name):
   message = "Hello, " + name + "!"
   return message

# Scenario 3: Function call with print
print(greet("Alice"))

