# for eachPass in range(4):
    #print("It's alive!", end = " ")  #To print everything in 1 line with a space between each
#     print("It's alive!", sep = " ") #Prints each sentence on a new line
    #print(eachPass + 1) #Prints on new line with numbers 1-4 listed
    #print(eachPass)#Prints from 0 to 3

number = 3
exponent = 2
product = 1
for eachPass in range(exponent):
    product = product * number

printText = f"The value of {number} to the power of {exponent} is {product}"
#make sure the print statement doesn't run inside the loop so that it doesn't repeat the amount of times that exponent is equal to.
print(printText)
