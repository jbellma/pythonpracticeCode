# Positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword arguments
describe_pet(animal_type='hamster', pet_name= 'harry')
describe_pet(pet_name= 'harry', animal_type= 'hamster')

# Default values
def describe_pet(pet_name, animal_type = 'dog'): # Order of parameters in the function definition had to be changed (Python still interprets this as a positional argument)
    """Display information about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name = 'willie')
describe_pet('willie')
describe_pet(pet_name = 'harry', animal_type= 'hamster')
