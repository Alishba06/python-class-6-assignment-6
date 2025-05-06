# file = open("myfile.txt","w") 

# file.write("Aaj ka din acha tha.\n")

# file.write("kal aur bhi acha hoga.\n")

# file.close()


# with open("myfile.txt","w") as file:

#          file.write("Aaj ka din acha tha.\n")

#          file.write("kal aur bhi acha hoga.\n")

#          file.close()



# multiple lines

# lines = ["Line 1\n" , "Line 2\n"]

# file = open("diary.txt" , "a")
# file.writelines(lines)
# file.close



# Read

# file = open("diary.txt", "r")

# print(file.read())

# file.close


# file = open("diary.txt", "r")

# for line in file:
#     print(line.strip())

# file.close


# with open("diary.txt","r") as file:
#     print(file.read())



# Exception Handling  Crash Se Bachaao

# try:
#     with open("unknown.txt","r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File nahi mili.")

# except Exception as e:
#     print(f"Kuch aur problem hui:{e}")




# Final Example

with open("final.txt" , "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

with open("final.txt" , "r") as f:
    print(f.read())

with open("final.txt", "a") as f:
    f.write("Line 3\n")

with open("final.txt", "r+") as f:
    f.seek(0)
    print("Final line:" , f.readline())