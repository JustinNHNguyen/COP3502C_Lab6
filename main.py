import encoder as encoder
import decoder as decoder


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
            password = encoder.encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded = decoder.decode(password)
            print("The encoded password is " + password + ", and the original password is " + decoded + ".\n")


if __name__ == '__main__':
    main()