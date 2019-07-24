from sys import argv

script,filename=argv

txt=open(filename)

print(f"here is the file name:{filename}")
print(txt.read())

print("Enter the name of file you wanna open")
file_again=input(">")
txt_again=open(file_again)
print(txt_again.read())