# 3 - Break Out of the Pattern


# Exercise 1
# Run in an infinite loop until the user types "q" or "Q"
while True:
    my_input = input('Type "q" or "Q" to quit: ')
    if my_input.upper() == "Q":
        break


# Exercise 2
# Display every number from 1 through 50 except multiples of 3
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)