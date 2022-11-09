Name = input("Please enter your name: ")
Surname = input("Please enter your surname: ")

SubName = str(Name) + " " + str(Surname)
SubName = SubName + "\n"

w = open("Names.txt", "a+")
w.writelines(SubName)
w.close()

UserName = Name[0] + Surname + "\n"
print(UserName)

r = open("Users.txt", "a+")
r.writelines(UserName)
print(r.read())
