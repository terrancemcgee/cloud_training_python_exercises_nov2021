
# Define the function
def greet(firstName, lastName):
  print("Hello " + firstName + " " + lastName)

# Call the function with positional arguments 
greet('Lenz', 'Paul')

# Call the function with named arguments. They don't have to be in order.
greet(lastName="Paul", firstName="Lenz")
