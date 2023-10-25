string = input("Enter the string to be encrypted: ")
key = int(input("Enter the key to be encrypted with: "))

print("Your Encrypted string is: ", end="")
for char in string:
    if char.isalpha():  # Check if the character is an alphabet letter
        shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        print(shifted_char, end="")
    else:
        print(char, end="")
