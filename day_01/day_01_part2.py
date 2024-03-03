# Open file in reading mode
input_file = open("day_01/input.txt", "r")

# Read each line as a string and attach it to the content array
input_content = input_file.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
           "1", "2", "3", "4", "5", "6", "7", "8", "9"]

calibration_values = []

for input_line in input_content: 
    first_digit_str = ""
    last_digit_str = ""

    min_index = len(input_line)
    max_index = 0

    for num in numbers:
        if num in input_line:
            if (min_index > input_line.find(num)):
                min_index = input_line.find(num)
                first_digit_str = num

            if max_index <= input_line.rfind(num):
                max_index = input_line.rfind(num)
                print
                last_digit_str = num

    # Translate string numbers to integers
    first_digit = 0
    last_digit = 0
    if first_digit_str != "":
        if numbers.index(first_digit_str) < 9:
            first_digit = numbers.index(first_digit_str) + 1
        else:
            first_digit = numbers.index(first_digit_str) - 8

    if last_digit_str != "":
        if numbers.index(last_digit_str) < 9:
            last_digit = numbers.index(last_digit_str) + 1
        else:
            last_digit = numbers.index(last_digit_str) - 8
    
    
    # Calibration value is found by combining the first digit and the last digit (in that order) to form a single two-digit number
    calibration_val = first_digit*10 + last_digit
    calibration_values.append(calibration_val)

print(calibration_values)

challenge_result = sum(calibration_values)

print(challenge_result)