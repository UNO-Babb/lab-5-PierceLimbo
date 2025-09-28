# Pierce Limbo ChaesarCipher 9/28/2025
#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): 
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: 
            secret = secret + letter

    return secret

def decode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    plain = ""

    for letter in message:
        if (alpha.find(letter) >= 0):  
            spot = (alpha.find(letter) - key) % 26  
            plain = plain + alpha[spot]
        else:  
            plain = plain + letter

    return plain
    
def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print ("Encrypted:", secret)

if __name__ == '__main__':
  main()


if __name__ == '__main__':
  main()
