#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

with open("winola.txt", "r") as file:
    content = file.read()

    with open("output1.txt", "w") as file:
        file.write(f"{content}\n")
        file.write("This is the output file\n")
        file.write("We are going to become a programmer soon\n")

#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

info = input("What file do you want to open?")

try:
    with open(info, "r") as file:
        content= file.read()
        print(content)  
        
except FileNotFoundError:
    print("File not found")
except IsADirectoryError:
    print("The path is a directory, not a file")
except Exception as e:
    print("An error occurred:", e)

else:
    with open("output1.txt", "w") as file:
        file.write(f"{content}\n")
        file.write("This is the output file\n")
        file.write("We are going to become a programmer soon\n")