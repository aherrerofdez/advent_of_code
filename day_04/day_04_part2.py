# Open file
with open("day_04/input.txt", "r") as input_file:
    # Read each line as a string and remove newline characters
    input_content = input_file.read().splitlines()

# Initialize an empty list to store the number of matches for each card
matches_array = []

# Iterate over each line in the input content
for input_line in input_content:
    # Split the line once and unpack the results
    winning_numbers_str, numbers_obtained_str = input_line.strip().split(" | ")
    # Extract winning numbers and obtained numbers as sets
    winning_numbers = set(winning_numbers_str.split(": ")[1].split())
    numbers_obtained = set(numbers_obtained_str.split())
    
    # Count matches using set intersection and append the count to the matches_array
    matches_array.append(len(winning_numbers & numbers_obtained))

# Create a dictionary where keys are card indices and values are the number of matches for each card
cards = dict(list(enumerate(matches_array)))

# Initialize the total number of cards
cards_number = len(cards)

# Define a function to recursively check for additional cards with matches
def check_cards_double(cards_double_sets, cards_number):
    # Iterate over card indices
    for i in cards_double_sets:
        # If the number of matches for a card is not zero
        if cards_double_sets[i] != 0:
            # Create a temporary dictionary for cards with double matches
            cards_double_temp = dict(list(cards.items())[i+1:i+cards[i]+1])
            # Update the total number of cards with double matches
            cards_number += len(cards_double_temp)
            # Recursively check for additional cards with matches
            cards_number = check_cards_double(cards_double_temp, cards_number)
    return cards_number

# Iterate over card indices
for i in cards:
    # If the number of matches for a card is not zero
    if cards[i] != 0:
        # Create a dictionary for cards with double matches
        cards_double = dict(list(cards.items())[i+1:i+cards[i]+1])
        # Update the total number of cards with double matches
        cards_number += len(cards_double)
        # Recursively check for additional cards with matches
        cards_number = check_cards_double(cards_double, cards_number)

# Print the final result, which is the total number of cards with matches
print(cards_number)

# Solution: 11827296
