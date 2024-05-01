# Open the input file in read mode
with open("day_02/input.txt", "r") as input_file:
    # Read each line from the file, removing newline characters
    input_content = input_file.read().splitlines()

# Initialize the variable to store the sum of the game ids
game_ids_sum = 0

# Define color limits
color_limits = {'r': 2, 'g': 3, 'b': 4}

# Iterate over each line in the input content
for input_line in input_content:
    # Extract the game id by splitting the string
    game_id = int(input_line.split(":")[0][5:])
    
    # Extract the sets obtained in each game by splitting the string
    game_sets = input_line.split(":")[1].strip()

    # Initialize a variable to check if the game is possible
    game_possible = True

    # Check if the game is not possible
    for idx, char in enumerate(game_sets):
        # Check all sets of balls that are equal to or more than 10
        if char.isdigit() and game_sets[idx+1].isdigit():
            # The game is not possible if there are 20 or more balls of any color
            if int(char) > 1:
                game_possible = False
                break
            # Check the units of each color against their limit 
            else:
                color = game_sets[idx+3]
                if color in color_limits and int(game_sets[idx+1]) > color_limits[color]:
                    game_possible = False
                    break

    # If the game has passed the checks, add the game id
    if game_possible:
        game_ids_sum += game_id

# Print the final result, which is the sum of game ids for possible games
print(game_ids_sum)

# Solution: 2317
