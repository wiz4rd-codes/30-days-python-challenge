import string
password = input("Enter your password : ")
strength = 0 
if(len(password)>=8):
    strength +=1
done1  = False
done2 = False
done3 = False
done4 = False
for ch in password:
    if(ch.isupper() and not done1):
        strength +=1
        done1 = True
    
    if(ch.islower() and not done2) :
        strength +=1 
        done2 = True
    
    if(ch.isdigit() and not done3):
        strength +=1
        done3 = True
    if(ch in string.punctuation and not done4):
        strength +=1
        done4 = True

if(strength>4):
    print("Strong Password ")
elif(strength >2 and strength<=4):
    print("Medium Password")
else : 
    print("Weak Password")
    
    
