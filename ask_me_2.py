# try:
#     name = input("Please Enter your name ")
#     print("Hello, " , name)
# except ValueError:
#     print("Hello, stranger.")
# we prompt a user to enter their name 
name = input("Enter the name: ")
# incase the user doesn't enter a name 
# the program prints hello stranger 
# incase name is entered it prints hello and the users name 
if name == "":
    print ("Hello Stranger")
else:
    print("Hello ",name)
