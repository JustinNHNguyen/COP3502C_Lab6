# By: Justin Nguyen
def encode(password):
    encoded = ""
    for i in range(0, len(password)):
        if int(password[i]) > 6:
            encoded += str((int(password[i]) + 3) % 10)
        else:
            encoded += str(int(password[i])+3)
    return encoded
