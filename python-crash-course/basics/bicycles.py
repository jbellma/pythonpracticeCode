bicycles = ['trek', 'canondale', 'redline', 'specialized']
#Accessing elements in a list
print(bicycles)
print(bicycles[0])

# Using string methods on list elements
print(bicycles[0].title())

# AIndex positions start at 0, not 1
print(bicycles[1])
print(bicycles[3])

# Asking for the last element in the list
print(bicycles[-1])

# Using individual values from a list
message = f"My first bycicle was a {bicycles[0].title()}."
print(message)
