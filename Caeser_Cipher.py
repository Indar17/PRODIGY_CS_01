#Caeser Cipher


#List of letters to check and encrypt the message
lowerc="abcdefghijklmnopqrstuvwxyz"
upperc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#Encryption Function
def encrypt(plaintext, shift):
    ciphertext=''
    for char in plaintext:
        if char in lowerc:
            eindex=(lowerc.find(char)+shift)%26
            ciphertext+=lowerc[eindex]
            
        elif char in upperc:
            eindex=(upperc.find(char)+shift)%26
            ciphertext+=upperc[eindex]
            
        else:
            ciphertext+=char
            
    return ciphertext

#Decryption Function
def decrypt(ciphertext, shift):
    plaintext=''
    for char in ciphertext:
        if char in lowerc:
            eindex=(lowerc.find(char)-shift)%26
            plaintext+=lowerc[eindex]
            
        elif char in upperc:
            eindex=(upperc.find(char)-shift)%26
            plaintext+=upperc[eindex]
            
        else:
            plaintext+=char
            
    return plaintext

print("Welcome to The Cipher Box")
choice= input("Enter e to encrypt or d to decript: ").lower()
i = 0 
while i<1:
    if choice == "e":
        plaintext = input("Enter a string to Encrypt: ")
        shift = int(input("Enter Shift Key: "))
        encrypted_text = encrypt(plaintext, shift)
        print("Encrypted Text: ", encrypted_text)
        i=+1
    elif choice=="d":
        ciphertext = input("Enter encrypted text: ")
        shift = int(input("Enter Shift Key: "))
        decrypted_text = decrypt(ciphertext, shift)
        print("Decrypted Text: ", decrypted_text)
        i+=1
    else:
        print("Wrong input value")


