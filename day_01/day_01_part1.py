# Open file in reading mode
input_file = open("day_01/input.txt", "r")

# Read each line as a string and attach it to the content array
input_content = input_file.readlines()

calibration_values = []

for input_line in input_content: 
    first_digit = 0
    last_digit = 0

    # Check all characters in the string from left to right until the first integer is found
    for char in input_line:
        if char.isnumeric():
            first_digit = int(char)
            break

    # Check all characters in the string from right to left until the first integer is found
    for char in input_line[::-1]:
        if char.isnumeric():
            last_digit = int(char)
            break
    
    # Calibration value is found by combining the first digit and the last digit (in that order) to form a single two-digit number
    calibration_val = first_digit*10 + last_digit
    calibration_values.append(calibration_val)

challenge_result = sum(calibration_values)

print(challenge_result)

# Solution: 55834
