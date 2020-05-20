def factorial(fak):
    count=1
    
    for item in range(fak):
        count=count*(item+1)
    
    return count  


tempList = []
keyList = []
cipperAsci = []


print("enter the plaintext")
plaintext = input()



for index,item in enumerate(plaintext):
    
    tempAsci = ord(item)
    tempCount = int((tempAsci * pow(2,index) * factorial(index+1)) / factorial(index))

    cipperAsci = tempCount % 255

    print("Aboodh Hali: " + tempCount)



    #print(str(index) + "item:" + item + " ascii:" + str(ord(item)))
    #tempList.append(item)




print(factorial(0))

#print("girilen değer:" + plaintext)