# Open the input file in read mode
with open("day_03/input.txt", "r") as input_file:
    # Read each line from the file, removing newline characters
    input_content = input_file.read().splitlines()

# Initialize arrays and variables
input_array = []  # Store the input characters as a matrix
symbols = "#$%&*+-/=@"  # Define symbols to look for in the input
symbols_index_array = []  # Store the indices of symbol characters
max_i_index = len(input_content) - 1  # Maximum row index
max_j_index = len(input_content[0]) - 1  # Maximum column index

# Create a matrix for the input characters
for input_line in input_content:
    input_array.append(list(input_line))

# Get indexes of symbol characters in the array
for i, row in enumerate(input_array):
    for j, item in enumerate(row):
        if item in symbols:
            symbols_index_array.append([i, j])

# Function to obtain the whole number adjacent to a symbol character
def get_whole_number(i, j):
    num = input_array[i][j]  # Initialize the number with the symbol itself
    temp_j = j
    # Traverse left to get the complete number
    while temp_j > 0 and input_array[i][temp_j-1].isnumeric():
        num = input_array[i][temp_j-1] + num
        temp_j -= 1
    # Traverse right to get the complete number
    while j < max_j_index and input_array[i][j+1].isnumeric():
        num = num + input_array[i][j+1]
        j += 1
    return num

# Initialize sum of neighboring numbers
part_numbers_sum = 0

# Check characters around each symbol to locate neighboring numbers
for symbol_index in symbols_index_array:
    part_numbers = []  # Store the neighboring part numbers

    # Check adjacent cells for numeric values
    for adjacent_cell_i in range(-1, 2):
        for adjacent_cell_j in range(-1, 2):
            # Skip the symbol itself
            if adjacent_cell_i == 0 and adjacent_cell_j == 0:  
                continue

            num_i, num_j = symbol_index[0] + adjacent_cell_i, symbol_index[1] + adjacent_cell_j
            if 0 <= num_i <= max_i_index and 0 <= num_j <= max_j_index and input_array[num_i][num_j].isnumeric():
                part_number = get_whole_number(num_i, num_j)
                part_numbers.append(int(part_number))
    
    # Add the sum of neighboring part numbers to the total sum
    part_numbers_sum += sum(set(part_numbers))

# Print the final result, which is the sum of neighboring part numbers
print(part_numbers_sum)

# Solution: 520135
