#This week we will create a program that performs file processing activities.  
# Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.  
# Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.  
# The program should then prompt the user for their name, address, and phone number.  
# Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user. 
#Once the data has been written your program should read the file you just wrote to the file system 
# and display the file contents to the user for validation purposes. 
#Submit a link to your Github repository.
import  os
filePath  =  input('Please enter a specified directory...') #/users/evanw/OneDrive/Desktop/python_work/ 
fileName  =  input('what is the file name you would like to create? ')
completePath  =  filePath+fileName
if  os.path.isdir(filePath): 
    print('This directory does in fact exist')
userName = input('What is your name? ') 
userAddress = input('What is your address? ')
userPhone = input('What is your phone number? ')
with open(completePath,  'w')  as  fileHandle: 
    fileHandle.write(userName + ', ' + userAddress + ', ' + userPhone) 
with open(completePath,  'r')  as  fileHandle: 
    addressBook  =  fileHandle.read()
    print(addressBook)