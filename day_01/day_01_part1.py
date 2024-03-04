# Open file
with open("day_01/input.txt", "r") as input_file:
    # Read each line as a string and remove newline characters
    input_content = input_file.read().splitlines()

# Initialize the variable to store the sum of calibration values
challenge_result = 0

for input_line in input_content:
    # Initialize variables to track the first and last digits
    first_digit, last_digit = None, None

    # Find and set both the first and last digits
    for char in input_line:
        if char.isdigit():
            # Update the first digit if not set
            if first_digit is None:
                first_digit = int(char)
            
            # Update the last digit on each iteration
            last_digit = int(char)

    # Check if both digits are found before calculating the calibration value
    if first_digit is not None and last_digit is not None:
        # Calculate the calibration value and add it to the result
        calibration_val = first_digit * 10 + last_digit
        challenge_result += calibration_val

# Print the final result
print(challenge_result)

# Solution: 55834
