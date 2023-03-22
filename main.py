# By: Justin Nguyen

def encode(password):

    return 0


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
            password = int(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decode(password)


if __name__ == '__main__':
    main()