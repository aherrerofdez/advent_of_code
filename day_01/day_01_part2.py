# Open the input file in read mode
with open("day_01/input.txt", "r") as input_file:
    # Read each line from the file, removing newline characters
    input_content = input_file.read().splitlines()

# Create a dictionary to map the number strings to integers
number_mapping = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
}

# Initialize the variable to store the sum of calibration values
challenge_result = 0

# Iterate over each line in the input content
for input_line in input_content:
    # Initialize variables to track the first and last digits
    first_digit_str, last_digit_str = "", ""

    min_index = len(input_line)  # Initialize min_index with a large value
    max_index = 0  # Initialize max_index with 0

    # Check if any digit or spelled number is in the string
    for num in number_mapping:
        if num in input_line:
            idx = input_line.find(num)  # Find the first occurrence of the number
            if min_index > idx:
                min_index = idx  # Update min_index if a smaller index is found
                first_digit_str = num  # Update first_digit_str with the corresponding number
            idx = input_line.rfind(num)  # Find the last occurrence of the number
            if max_index <= idx:
                max_index = idx  # Update max_index if a larger or equal index is found
                last_digit_str = num  # Update last_digit_str with the corresponding number

    # Translate string numbers to integers using the dictionary
    first_digit = number_mapping.get(first_digit_str, 0)  # Get the integer value for the first digit
    last_digit = number_mapping.get(last_digit_str, 0)  # Get the integer value for the last digit

    # Calculate the calibration value and add it to the result
    calibration_val = first_digit * 10 + last_digit  # Combine the first and last digits
    challenge_result += calibration_val  # Add the calibration value to the challenge result

# Print the final result, which is the sum of calibration values
print(challenge_result)

# Solution: 53221
