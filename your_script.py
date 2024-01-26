# your_script.py
# your_script.py

# Importing necessary modules
import math
import random

# Define a function that performs some computation
def calculate_square_root(number):
    return math.sqrt(number)

# Define another function that generates a random number
def generate_random_number():
    return random.randint(1, 100)

# Create a main method to orchestrate the flow of your program
def main():
    # Example usage of the defined functions
    input_number = 25
    result = calculate_square_root(input_number)
    print(f"The square root of {input_number} is: {result}")

    random_num = generate_random_number()
    print(f"Generated random number: {random_num}")

# Add conditional execution logic
if __name__ == "__main__":
    # Execute main() only if the script is run directly
    main()
