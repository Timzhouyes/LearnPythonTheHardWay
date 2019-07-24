# This file is for Reading and Writing files.

from sys import argv

script,filename=argv

print(f"We are going to erase the{filename}")
print("If you don't want to do it, hit CTRL-C")
print("If you want to do it, hit RETURN")

input("?")

print("Opening file ")
target=open(filename,"w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am asking you for 3 lines")
line1=input("Line 1")
line2=input("Line 2")
line3=input("Line 3")

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally we close it")
target.close()