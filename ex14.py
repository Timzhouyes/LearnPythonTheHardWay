from sys import argv

script, user_name=argv
prompt='>'

print(f"Hi{user_name},I am the {script} script")
likes=input("So what do you think about me \n >")

print(f"Oh so you think {likes} about me!")