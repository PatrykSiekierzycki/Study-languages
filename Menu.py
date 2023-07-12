import os, LoadFiles

"""
Brief: Class responsible for show menu and getting data from user.
"""
class Menu:

    """
    Brief: Ask user abaut option. Then call proper method.
    Param: None.
    Return: None.
    """
    def __init__(self):
        menu_0 = """Welcome in program for learn languages. 
Choose a number of option:
1. Log in.
2. Sign in.
Option: 
"""
        # Input protection.
        choosed_option = 0
        flag1 = True
        while flag1:
            choosed_option = int(input(menu_0))
            if choosed_option < 1 or choosed_option > 2:
                print("Incorrect data! Try again!\n")
            else:
                flag1 = False



        # Call in proper method according to user choice.
        if choosed_option == 1:
            self.log_in()
        elif choosed_option == 2:
            self.sign_in()

    """
    Brief: Ask user about data. Check them and add to database file.
    Param: None
    Return: None
    """
    def sign_in(self):

        username = input("Give Username: ")


        # Check if there is no the username in users db.
        while self.check_in_user_db(username, 1):
            username = input("The user input already exist. Choose another one: ")

        # Get data from user.
        native_language = input("Give your native language: ")
        password = input("Give password: ")
        repeated_password = input("Repeat password: ")

        # Check the passwords
        flag_1 = False
        while flag_1 is False:  # Untill both "passwoerd" and "repeated_password" isn't the same.

            if password != repeated_password:  # If repeated password is not the same as previous.
                password = input("""The passwords is not the same. Try again. "
                                 "Give password: """)
                repeated_password = input("Repeat password: ")
            elif password == repeated_password:  # If password is the same as previous.
                flag_1 = True  # Change flag and finish loop.

            # Protection before unexisted file
            if not os.path.exists("users/users_database.txt"):  # If file don't exist
                file_0 = open("users/users_database.txt", "x")  # Create and open file
                file_0.close()  # Then close that file.

            # Get number of sign users.
            how_many_user = 0  # How many users are sign in.
            with open("users/users_database.txt", "r") as file_1:  # Open "users_database.txt" file for read.
                for line in file_1:  # Loop through data from "users_database.txt" file.
                    how_many_user += 1  # For each list (that means each user (line = user)) increment variable "how_many_user". It is for get information about number of users.

            # Save data into users db file
            with open("users/users_database.txt", "a") as file_2:  # Open "users_database.txt" file for append.
                how_many_user = str(how_many_user + 1)  # Creat number of index for new user.
                file_2.write(how_many_user + "=" + username + "=" + native_language + "=" + password + "\n")  # Append all user data into "users_database.txt" file.

            os.chdir("users")  # Change localization to "users" catalogue.
            os.mkdir(username)  # Create new catalogue for new user, with name as user's login.
            os.chdir("..")  # Change localization to main catalogue.
            print("Datas already append to database.")

    """
    Brief: Open users db. Check if data as first param, exist in file at 'what_data' position. Return True if exist, and False if not.
    Param: data - each type, what_data - int (0-3).
    Return: flag - bool, also can return all data by username.
    """
    # what_data: 0 = index, 1 = username (login), 2 = native_language, 3 = password
    def check_in_user_db(self, data, what_data, all_data = False):

        flag = False

        # Protection before unexisted file
        if not os.path.exists("users/users_database.txt"):  # If file dosen't exist
            file_0 = open("users/users_database.txt", "x")  # Creat and open file
            file_0.close()  # Close the file.

        all = []  # List for all line from db file

        with open("users/users_database.txt", "r") as file_1:  # Open "users_database.txt" for read.

            # Check all file by getted value and return True if exist, False if not, also can added return all data by geted data.
            for line in file_1:
                user_data = line.rsplit("=")  # Separate line from file

                if what_data == 0:  # Check only first datas (indexes).
                    if data == int(user_data[what_data]):  # If proper index already exist in file "users_database.txt"
                        all.append(user_data)  # Append all data to list "all"
                        flag = True  # Finish loop.
                elif what_data == 1:  # Check only second datas (username).
                    if data == user_data[what_data]:# If proper login already exist in file "users_database.txt"
                        all.append(user_data)  # Append all data to list "all"
                        flag = True  # Finish loop.
                elif what_data == 2:  # Check only third datas (native_language).
                    if data == user_data[what_data]:  # If proper native language already exist in file "users_database.txt"
                        all.append(user_data)  # Append all data to list "all"
                        flag = True  # Finish loop.
                elif what_data == 3:  # Check only fourth datas (password).
                    if data == user_data[what_data]:  # If proper password already exist in file "users_database.txt"
                        all.append(user_data)  # Append all data to list "all"
                        flag = True  # Finish loop.

        # User decide if want return only bool or also all datas by username
        if all_data is False:  # If specified data are not in "users_database.txt" file
            return flag  # Return False
        else:
            return flag, all  # Return True and all data


    """
    Brief: Get login's data from user. Check are they correct. Change location on user's catalog.
    Param: None.
    Return: None. At the end call LoadFiles method from LoadFiles.py file and give "username" variable as argument
    """
    def log_in(self):

        flag = False

        # Untill program don't get from user proper login's data to log in.
        while flag == False:
            # Get login's data from user.
            username = input("Get username: ")
            password = input("Get password: ")

            d_1, line = self.check_in_user_db(username, 1, all_data=True)  # Check if in "users_database.txt" file exist a username getting from user. Also return all data.


            # Check datas and decide about succesfully log in.
            if d_1 is False:  # If there is no user's "username" in "users_database.txt" file.
                decision = input("Access denied! Do you want to exit program? (y/n): ")  # Get info from user if he want to try again or not.
                if decision == "y": exit(0)  # If user don't want to log in again, exit program.
            else:  # If user want to try log in again.
                setted_password = line[0][3]  # Get password to user's account.
                setted_password = setted_password[:-1]  # Remove the new line sign at end of users data.

                if password != setted_password:  # If password are not the same as setted password.
                    decision = input("Access denied! Do you want to exit program? (y/n): ")  # Get info from user if he want to try again or not.
                    if decision == "y": exit(0)  # If user don't want to log in again, exit program.
                else:  # If password are the same as saved into users db .txt file.
                    flag = True  # Finish loop.
                    print("Access granted.")

                os.chdir("users/" + username)  # Change localization to user's catalogue.
                object_loadFiles = LoadFiles.LoadFiles(username)  # Create "LoadFiles.LoadFiles" object and provide to it a username.
