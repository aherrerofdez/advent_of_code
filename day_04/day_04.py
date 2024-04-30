# Open file
with open("day_04/input.txt", "r") as input_file:
    # Read each line as a string and remove newline characters
    input_content = input_file.read().splitlines()

total_points = 0

for input_line in input_content:
    # Split the line once and unpack the results
    winning_numbers_str, numbers_obtained_str = input_line.strip().split(" | ")
    # Extract winning numbers and obtained numbers as sets
    winning_numbers = set(winning_numbers_str.split(": ")[1].split())
    numbers_obtained = set(numbers_obtained_str.split())
    
    # Count matches using set intersection
    matches = len(winning_numbers & numbers_obtained)

    # Calculate points
    points = 2**(matches-1) if matches > 0 else 0
    total_points += points

# Print the final result
print(total_points)

# Solution: 21568
