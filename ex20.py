from sys import argv

script, input_file=argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(linecount,f):
    print(linecount,f.readline(),end=" ")

current_file=open(input_file)

print("First type whole file")
print_all(current_file)

print("Now get back to the 1st line of file")
rewind(current_file)

print("Then just show how to write file line by line")

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)