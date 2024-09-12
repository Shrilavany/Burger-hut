import math

turn1 = int(input())  # Example value for turn1 (number of dishes)
turn2 = int(input())  # Example value for turn2 (number of branches)

# Calculate total chances
total_chances = math.ceil(math.log (turn2 - turn1 + 1, 2))

print("Total Chances:",total_chances)