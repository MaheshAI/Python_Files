import random
import string

# Define the characters to choose from
characters = string.ascii_letters + string.digits

# Generate a random string of 8 characters
random_string = ''.join(random.choices(characters, k=8))

# Print the random string
print("Random String:", random_string)
