while True:
    import random
    import string
    length = int(input("Enter the length of password: "))
    if length <= 0:
        print("Please enter a positive number!")
        continue
    print(length)
    characters = string.ascii_letters + string.digits + string.punctuation
    print(characters)
    password = " "
    for i in range (length):
        random_char = random.choice(characters)
        password = password + random_char
    print("Generated Password:", password)
    again = input(" Do you want to generate another password? (y/n): ")
    if again.lower() != "y":
        break
print(" Thanks for generate the password. Have a nice day!")