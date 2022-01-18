"""
This is a program that will allow users to create an account name.
Its job is to prevent two accounts with the same name.
Written on 20 June, 2020
"""
loop = 5
user_names = ["sam", "sammy", "samuel", "samsam"]
#----------------------------------------------------------------------------------------------------------------------
#VERSION 4
while loop == 5:
    username = str(input())

    if username in user_names:
        print("This user name has already been chose\n Please choose another one")
        continue
    else:
        print("This username works\nWELCOME " + (username))
        user_names.append(username)
        break
#----------------------------------------------------------------------------------------------------------------------
#VERSIONN 3
"""
while loop == 5:
    username = str(input())
    user_filter = len(list(filter(lambda x: username in user_names, user_names)))

    if user_filter == 0:
        print("This username works\nWELCOME " + (username))
        user_names.append(username)
    else:
        print("This user name has already been chose\n Please choose another one")
"""
#----------------------------------------------------------------------------------------------------------------------
#VERSION 2
"""
i = 0
while loop == "fun":
    username+str(i) = str(input)
    user_filter = len(list(filter(lambda x: username+str(i) in user_names, user_names)))

    if user_filter == 0:
        print ("This username works\nWELCOME "+ (username+str(i)))
        user_names.append(username+str(i))
    else:
        print("This user name has already been chose\n Please choose another one")
    i = i+1
"""
#----------------------------------------------------------------------------------------------------------------------
#VERSION 1
"""
username1 = "Samuel"
username2 = "Sammy"
username3 = "Sam"
username4 = "YES"

user_names = [username1, username2, username3]
user_filter = len(list(filter(lambda x: x==username4, user_names)))

if user_filter == 0:
    print ("This user name works\nWELCOME "+username4)
    user_names.append(username4)
else:
    print ("This user name has already been used, please try a different user name")
"""