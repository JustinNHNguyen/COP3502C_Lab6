# By: Justin Nguyen

def encode(password):
    encoded = ""
    for i in range(0, len(password)):
        if int(password[i]) > 6:
            encoded += str((int(password[i]) + 3) % 10)
        else:
            encoded += str(int(password[i])+3)
    return str(encoded)


def main():
    option = 0
    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decode(password)


if __name__ == '__main__':
    main()