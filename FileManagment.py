file=open("tops1.txt","w")
file.write("This Is file managment demo using python.")
file.close()
print("file written successfully")
print("*****************************")


file=open("tops1.txt","r")
print(file.read())
file.close()
print("*****************************")


file=open("tops1.txt","a")
file.write("\nThis file is now appeded.")
file.close()
print("file appended successfully")
print("*****************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*****************************")


file=open("tops2.txt","w+")
file.write("This is w+ mkode uing python.")
print("file current position : ",file.tell())
file.seek(0)
print(file.read())
file.close()
print("*****************************")






