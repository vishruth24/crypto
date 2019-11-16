def encrypt(text,s): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
    return result 
  
text=raw_input("Enter the text:")
text=text.replace(" ","")

for i in range(0,26):
    print "Decryption ["+str(i)+"]: " + encrypt(text,i) 