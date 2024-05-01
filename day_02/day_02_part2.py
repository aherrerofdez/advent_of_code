# Open the input file in read mode
with open("day_02/input.txt", "r") as input_file:
    # Read each line from the file, removing newline characters
    input_content = input_file.read().splitlines()

# Define a list of colors
colors = ["blue", "green", "red"]

# Initialize the sum of game powers
game_powers_sum = 0

# Iterate over each line in the input content
for input_line in input_content:
    # Extract the sets obtained in each game by splitting the string
    game_sets = input_line.split(":")[1].strip()

    # Initialize the game power
    game_power = 1

    # Iterate over each color
    for color in colors:
        # Find occurrences of the color in the game sets
        color_in_game_set = [i for i in range(len(game_sets)) if game_sets.startswith(color, i)]

        # If the color is found in the game sets
        if color_in_game_set:
            min_num_color = 0
            # Iterate over each occurrence of the color
            for i in color_in_game_set: 
                # Check if there are at least 3 characters before the color and the character before is a digit
                if i >= 3 and game_sets[i-3].isdigit() and min_num_color < (int(game_sets[i-3])*10 + int(game_sets[i-2])):
                    min_num_color = int(game_sets[i-3])*10 + int(game_sets[i-2])
                else:
                    # If not, consider the current digit as the minimum
                    if min_num_color < int(game_sets[i-2]):
                        min_num_color = int(game_sets[i-2])
            
            # Update the game power by multiplying with the minimum number associated with the color
            game_power *= min_num_color

    # Add the game power to the sum of game powers
    game_powers_sum += game_power

# Print the final result, which is the sum of game powers
print(game_powers_sum)

# Solution: 74804
