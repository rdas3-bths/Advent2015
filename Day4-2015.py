
# Python 3 code to demonstrate the
# working of MD5 (byte - byte)

import hashlib

def check_five_zeros(hash):
    hash_list = hash.split("\\")
    if hash_list[1] == 'x00' and hash_list[2] == 'x00' and hash_list[3] == 'x00':
        return True
    return False

input = "bgvyzdsv"


# printing the equivalent byte value.

counter = 0
while True:
    hash = input + str(counter)
    result = hashlib.md5(hash.encode())
    result = check_five_zeros(str(result.digest()))
    counter += 1
    if result:
        print(hash + ": " + str(result))
        break
