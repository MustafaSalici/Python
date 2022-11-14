def main():
    # Open the file to write the name and surname data in write mode
    NameSurnameWrite = open("NameSurname.txt", "w")

    # Retrieving name and surname data from the user
    NameSurnameValue = input("Enter your first and last name with a space in between (press enter to end): ")
    while NameSurnameValue!="":
        print(NameSurnameValue, file=NameSurnameWrite)
        NameSurnameValue = input("Enter your first and last name with a space in between (press enter to end): ")

    # Open name and surname data in read mode
    NameSurnameWrite = open("NameSurname.txt", "r")

    # Open file to write usernames in write mode
    UserNameValue = open("UserName.txt", "w")

    # Get lines from file with name and surname data
    for line in NameSurnameWrite:
        # Split line by spaces and put in a list
        NameSurnameList = line.split(" ")

        # First element of the list name second element last name
        # Combine the first letter of the name with the last name and write it in the username list
        user = NameSurnameList[0][0] + NameSurnameList[1]
        print(user, file=UserNameValue)

main()