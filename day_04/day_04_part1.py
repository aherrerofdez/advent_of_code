# Open the input file in read mode
with open("day_04/input.txt", "r") as input_file:
    # Read each line from the file, removing newline characters
    input_content = input_file.read().splitlines()

# Initialize a variable to store the total points
total_points = 0

# Iterate over each line in the input content
for input_line in input_content:
    # Split the line once into winning and obtained numbers
    winning_numbers_str, numbers_obtained_str = input_line.strip().split(" | ")
    # Extract winning numbers and obtained numbers as sets
    winning_numbers = set(winning_numbers_str.split(": ")[1].split())
    numbers_obtained = set(numbers_obtained_str.split())
    
    # Count matches using set intersection
    matches = len(winning_numbers & numbers_obtained)

    # Calculate points based on the number of matches
    points = 2**(matches-1) if matches > 0 else 0
    # Add the points to the total points
    total_points += points

# Print the final result, which is the total points obtained
print(total_points)

# Solution: 21568
