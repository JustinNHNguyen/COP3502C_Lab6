
def decode(encoded_password):
    decoded_password = ''
    for i in encoded_password:
        if int(i) < 3:
            decoded_password += str(int(i) + 7)
        else:
            decoded_password += str(int(i) - 3)
    return decoded_password

