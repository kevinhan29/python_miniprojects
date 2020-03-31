secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

alphabet = "abcdefghijklmnopqrstuvwxyz"
# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
numbers = []
for i in range(len(alphabet)):
    numbers.append(i)
    # print(numbers)

# create cesar cypher shifted dictionary
cipher_dict = {}
for letter, num in zip(alphabet, numbers):
    # print(letter, num)
    index = num + cipher            # shifts index by cipher shift value
    if index < numbers[0]:          # wraps index around end of range if it goes out of lower bound
        index += numbers[-1]
    elif index > numbers[-1]:       # wraps index around to beginning of range if it goes out of upper bound
        index -= numbers[-1]
    cipher_dict[letter] = alphabet[index]   # assigns shifted letter to original letter
    # print(cipher_dict.keys(), "\n", cipher_dict.values())

# encoding the original message by using original letters as keys to find the ciphered value
secret = secret.lower()
ciphered_msg = ""
for letter in secret:
    if cipher_dict.get(letter) == None:             # don't cipher non-letter characters
        ciphered_msg = ciphered_msg + letter
        continue
    ciphered_msg = ciphered_msg + cipher_dict[letter]   # add ciphered character to message
    # print(ciphered_msg)

print(ciphered_msg)