def binary_to_decimal(binary):
    return int(binary, 2)

binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)

print("The decimal equivalent of", binary_input, "is", decimal_output)