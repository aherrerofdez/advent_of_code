# Open file
with open("day_02/input.txt", "r") as input_file:
    # Read each line as a string and remove newline characters
    input_content = input_file.read().splitlines()

# Initialize the variable to store the sum of the game ids
game_ids_sum = 0

color_limits = {'r': 2, 'g': 3, 'b': 4}

for input_line in input_content:
    # Extract the game id by splitting the string
    game_id = int(input_line.split(":")[0][5:])
    
    # Extract the sets obtained in each game by splitting the string
    game_sets = input_line.split(":")[1].strip()

    game_possible = True
    for idx, char in enumerate(game_sets):
        if char.isdigit() and game_sets[idx+1].isdigit():
            if int(char) > 1:
                game_possible = False
                break
            else:
                color = game_sets[idx+3]
                if color in color_limits and int(game_sets[idx+1]) > color_limits[color]:
                    game_possible = False
                    break

    if game_possible:
        game_ids_sum += game_id

# Print the final result
print(game_ids_sum)

# Solution: 2317
