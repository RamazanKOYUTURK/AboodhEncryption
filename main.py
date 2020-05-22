def factorial(fak):
    
    count=1
    
    for item in range(fak):
        count=count*(item+1)
    
    return count 


def encryption(plaintext):
    global cipperText
    tempCipperText = ""

    for index,item in enumerate(plaintext):
        tempAsci = ord(item)
        tempCount = int((tempAsci * pow(2,index) * factorial(index+1)) / factorial(index))
        keyList.append(int(tempCount/255))
        tempCipperText = tempCipperText + chr(tempCount % 255)
    
    cipperText = tempCipperText


def decryption(cipperText):
    global plaintext
    tempPlainText = ""

    for index,item in enumerate(cipperText):
        tempAsci = ord(item)
        tempCount = tempAsci + keyList[index]*255
        plaintextAsci = int((tempCount * factorial(index))/(pow(2,index)*factorial(index+1)))
        tempPlainText = tempPlainText + chr(plaintextAsci)

    plaintext = tempPlainText


tempList = []
keyList = []
cipperAsci = []
plaintextAsci = []

print("enter the plaintext")
plaintext = input()
encryption(plaintext)
print("Şifrelenmiş Metin: " + cipperText)
print("Anahtar Listesi:")
print(*keyList)
decryption(cipperText)
print("Çözülen Şifre: " + plaintext)