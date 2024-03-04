# Open file
with open("day_01/input.txt", "r") as input_file:
    # Read each line as a string and remove newline characters
    input_content = input_file.read().splitlines()

# Create a dictionary to map the number strings to integers
number_mapping = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
}

# Initialize the variable to store the sum of calibration values
challenge_result = 0

for input_line in input_content:
    # Initialize variables to track the first and last digits
    first_digit_str, last_digit_str = "", ""

    min_index = len(input_line)
    max_index = 0

    # Check if any digit or spelled number is in the string
    for num in number_mapping:
        if num in input_line:
            idx = input_line.find(num)
            if min_index > idx:
                min_index = idx
                first_digit_str = num
            idx = input_line.rfind(num)
            if max_index <= idx:
                max_index = idx
                last_digit_str = num

    # Translate string numbers to integers using the dictionary
    first_digit = number_mapping.get(first_digit_str, 0)
    last_digit = number_mapping.get(last_digit_str, 0)

    # Calculate the calibration value and add it to the result
    calibration_val = first_digit * 10 + last_digit
    challenge_result += calibration_val

print(challenge_result)

# Solution: 53221
