import random
a = input("Enter your message : ")
o = int(input("Enter 0 for Code\nEnter 1 for Decode\nEnter number : "))
words = a.split(" ")

print(words)

def code(words) :
    secret = []
    for word in words:
        if(len(word)>=3):
            r1 = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k = 3))
            r2 = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k = 3))
            
            b = r1 + word[1:]+word[0] + r2
            secret.append(b)
   
        else:
           secret.append(word[::-1])
    print(" ".join(secret))
def decode(words):
    decoded = []
    for word in words : 
        if(len(word)>= 3):
            b = word[-4] + word[3:-4]
            decoded.append(b)
        else: 
            b = word[::-1]
            decoded.append(b)
    print(" ".join(decoded))
if(o == 0):
    code(words)
else: 
    decode(words)

