import random

def generatePassword(letter_count,symbol_count,number_count):
    p_letters = random.sample(letters, letter_count)
    p_symbols = random.sample(symbols, symbol_count)
    p_numbers = random.sample(numbers, number_count)
    random_pass = "".join(p_letters) + "".join(p_numbers) + "".join(p_symbols)
    pass_list = list(random_pass)
    random.shuffle(pass_list)
    strong_pass = "".join(pass_list)
    return strong_pass

if __name__ == '__main__':

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password? "))
    nr_numbers = int(input(f"How many numbers would you like? "))
    nr_symbols = int(input(f"How many symbols would you like? "))

    print(generatePassword(letter_count=nr_letters,symbol_count=nr_symbols,number_count=nr_numbers))

