from ast import Return
import rsa as rsa


key = 0

key = input("Enter the Encryption Key: " )

while not key.isdigit():
    print("Invalid(Enter a number)")
    key = input("Enter the Encryption Key:")
else:
    print("Valid")

mod_value = input("Enter the Modulus: " )

while not mod_value.isdigit():
    print("Invalid(Enter a number)")
    mod_value = input("Enter the Modulus: ")
else:
    print("Valid")

plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)

# isalpha() will do the same as isdigit() but with alphabetic letters.