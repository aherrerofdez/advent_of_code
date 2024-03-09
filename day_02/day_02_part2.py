# Open file
with open("day_02/input.txt", "r") as input_file:
    # Read each line as a string and remove newline characters
    input_content = input_file.read().splitlines()

colors = ["blue", "green", "red"]

game_powers_sum = 0

for input_line in input_content:
    # Extract the sets obtained in each game by splitting the string
    game_sets = input_line.split(":")[1].strip()

    game_power = 1

    for color in colors:
        color_in_game_set = [i for i in range(len(game_sets)) if game_sets.startswith(color, i)]

        if color_in_game_set:
            min_num_color = 0
            for i in color_in_game_set: 
                if i >= 3 and game_sets[i-3].isdigit() and min_num_color < (int(game_sets[i-3])*10 + int(game_sets[i-2])):
                    min_num_color = int(game_sets[i-3])*10 + int(game_sets[i-2])
                else:
                    if min_num_color < int(game_sets[i-2]):
                        min_num_color = int(game_sets[i-2])
            
            game_power *= min_num_color

    game_powers_sum += game_power

# Print the final result
print(game_powers_sum)

# Solution: 74804
