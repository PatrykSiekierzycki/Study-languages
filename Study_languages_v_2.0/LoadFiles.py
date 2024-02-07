import os, CheckMechanism, Dates

"""
Class responsible for loading proper files.
"""
class LoadFiles:

    list_of_words = []
    dictionary_of_words = {}
    user_dict = {}
    # List of dictionaries files
    list_of_dictionary_files = [
        "dictionaries files\english - polish dictionary.txt", "dictionaries files\japanese - polish dictionary.txt",
        "dictionaries files\\romanian - polish dictionary.txt"]
    # List of user's file's name.
    list_of_users_dicts_file = ["My english words.txt", "My japanese words.txt", "My romanian words.txt"]

    def __init__(self, username):
        self.username = username
        # Show option
        language_menu = """Choose your language, and give the number: 
1. English - Polish
2. Japanese - Polish
3. Romanian - Polish
Give a number: """

        flag1 = True
        while flag1:
            self.option_number = int(input(language_menu)) # User's choosing language to study.
            if self.option_number > len(self.list_of_dictionary_files) or self.option_number < 0:
                print("Wrong number of option. Try again.")
            else:
                flag1 = False

        self.path_to_user_file = "users\\" + self.username + "\\" + self.list_of_users_dicts_file[self.option_number - 1] # Path to user's file with choosed language

        # Ask user about option
        question_about_repeats = """Choose number of option:
1. Learn new words
2. Repeat words
Give a number: """

        new_words_or_repeats = 0
        flag2 = True
        while flag2:
            new_words_or_repeats = input(question_about_repeats)
            is_numeric = new_words_or_repeats.isnumeric()
            if is_numeric:
                new_words_or_repeats = int(new_words_or_repeats)
                if new_words_or_repeats < 1 or new_words_or_repeats > 2:
                    print("Wrong number of option. Try again.")
                else:
                    flag2 = False

        # Call a proper method according to user's choice.
        if new_words_or_repeats == 1:
            self.learn_new_words()
        elif new_words_or_repeats == 2:
            self.repeat_words()

    """
    Brief: Change location at user file and call read_dict_file method.
    Param: int - number of option at choose language.
    Return: None.
    """
    def learn_new_words(self):
        # Change localization at main catalogue.
        os.chdir("..")
        os.chdir("..")
        self.file_name = self.list_of_dictionary_files[self.option_number - 1] # Name of user's choosed language file.
        self.read_dict_file()  # Call method "read_dict_file".

    """
    Brief: Change location at user file and call read_user_file.
    Param: int - number of option at choose language.
    Return: None.
    """
    def repeat_words(self):
        self.file_name = self.list_of_users_dicts_file[self.option_number - 1] # Name of user's choosed language file
        self.read_user_file()  # Call method "read_user_file".


    """
    Brief: open dictionary file and put all data from it, into dicts nested into list.
    Param: str - file_name - name of proper dictionary file.
    Return: None. 
    """
    def read_dict_file(self): # # Name of user's choosed language file.

        checkIndexInFile_object = CheckIndexInFile(self.path_to_user_file, self.file_name)  # Create an CheckIndexInFile's object. Provide path to users file and a name of file dictionary file.
        unlearned_words = checkIndexInFile_object.get_unlearned_words() # Get list of each unlearned word in dictionary.

        checkMechanism_object = CheckMechanism.Check_mechanism(self.username, unlearned_words, self.list_of_users_dicts_file, self.option_number)  # Creat a "CheckMechanism.Check_mechanism's" object.
        checkMechanism_object.check_mechanism_for_new_words()


    """
    Brief: open user file and put all data from it, into dicts nested into list.
    Param: str - file_name - name of proper user file.
    Return: None.
    """
    def read_user_file(self):

        # Protection before unexisted user file.
        if os.path.exists(self.file_name) is False:
            key = input("File dosen't exist! You should first choose an option to learn new words.")
            exit(1)

        # Preper list of dict from users file
        get_list_of_dicts_object = Get_list_of_dicts(self.file_name)
        flag, prepered_list = get_list_of_dicts_object.preper_list() # All word from user's file
        if flag is False:
            exit(0)
        lenght_of_finished_list = len(prepered_list) # How many words are in user's file

        # Check if words are to repeat.
        dates_object = Dates.Dates()  # Creat a "Dates.Dates" object.
        i = 0
        l_words_to_repeat = []  # The list of words to repeat
        while i < lenght_of_finished_list:

            response = dates_object.is_it_to_repeat(prepered_list[i]["date of repeat"])  # Is the actual "looping" word to repeat?

            if response is True:  # If word is to repeat
                l_words_to_repeat.append(prepered_list[i])  # Append al that word dict into "l_words_to_repeat" list.
            i += 1

        get_word_to_repeat_object = Get_word_to_repeat(self.file_name)  # Creat a "Get_word_to_repeat" object and provide to it a "file_name".
        get_word_to_repeat_object.update_users_file(l_words_to_repeat)


        checkMechanism_object = CheckMechanism.Check_mechanism(self.username,  l_words_to_repeat, self.list_of_users_dicts_file, self.option_number)
        checkMechanism_object.check_mechanism_for_repeats()


"""
Brief: Class responsible for getting dictionary list of unlearned word.
"""
class CheckIndexInFile:

    user_index_list = []
    unlearned_words = []

    def __init__(self, path_to_users_file, dict_file):
        self.dict_file = dict_file
        self.path_to_users_file = path_to_users_file

    """
    Brief: Get full list of unlearned words.
    Param: None.
    Return: Dict's list
    """
    def get_unlearned_words(self):
        # Protection before unexisting file.
        if not os.path.exists(self.path_to_users_file):  # If file dosen't exist
            file_0 = open(self.path_to_users_file, "x")  # Creat a file and open it.
            file_0.close()  # Close the file.

        # Get data from user's file and put it into "self.user_index_list" list.
        try:
            with open(self.path_to_users_file, "r", encoding="utf8") as file_0:
                for line in file_0:
                    line = line.rsplit("=")
                    self.user_index_list.append(line[0])

        except FileNotFoundError:
            key = input("File was not founded.")
            exit(1)
        except Exception:
            key = input("Problem was occur at attempt of open file.")
            exit(1)

        # Get list with dicts of unlearned words.
        datas_from_file = []

        try:
            with open(self.dict_file, "r", encoding="utf8") as file_0:  # Open dictionary file
                # Get data from file.
                for line in file_0:
                    datas_from_file.append(line.rsplit("="))

        except FileNotFoundError:
            key = input("File was not founded.")
            exit(1)
        except Exception:
            key = input("Problem was occur at attempt of open file.")
            exit(1)

        for line in datas_from_file:
            if line[0] not in self.user_index_list:  # If index of actual "looping" word is not into user's file
                new_word = {}
                new_word["index"] = line[0]
                new_word["foreign word"] = line[1]
                new_word["native translation"] = line[2][:-1]

                self.unlearned_words.append(new_word)

        return self.unlearned_words  # Return list with dicts of unlearned word.


"""
Brief: Class responsible for update user file.
"""
class Get_word_to_repeat:

    def __init__(self, users_file_name):
        self.users_file_name = users_file_name

    """
    Brief: Update repeted words datas into user's file.
    Param: List of dicts.
    Return: None
    """
    def update_users_file(self, updated_data):

        updated_list = updated_data  # It is a list with dicts of words to repeat.
        finished_list = []
        get_list_of_dicts_object = Get_list_of_dicts(self.users_file_name)  # Creat a "Get_list_of_dicts's" object.
        flag, unupdated_list = get_list_of_dicts_object.preper_list()  # Get a list with dicts of all words from user's file.

        if flag is False:
            key = input("There is a problem with file!")
            exit(0)

        # Append to "finished_list" list proper dicts
        for word in unupdated_list:
            if not word["index"] in updated_list:
                finished_list.append(word)
            elif word["index"] in updated_list:
                finished_list.append(updated_list.index(word["index"]))

        # Save data into user's file
        how_many_words = len(finished_list)
        if how_many_words > 0:  # Do only if is something to save.
            try:
                with open(self.users_file_name, "w", encoding="utf8") as file_0:
                    i = 0
                    while i < how_many_words:
                        file_0.write(str(finished_list[i]["index"]) + "=" + finished_list[i]["foreign word"] + "=" + finished_list[i]["native translation"] + "=" + str(finished_list[i]["number for repeat"]) + "=" + finished_list[i]["date of repeat"] + "\n")
                        i += 1
            except FileNotFoundError:
                key = input("File was not founded.")
                exit(1)
            except Exception:
                key = input("Problem was occur at attempt of open file.")
                exit(1)

"""
Brief: Get name of file and preper a list of dicts.
"""
class Get_list_of_dicts:

    def __init__(self, file_name):
        self.file_name = file_name

    """
    Brief: Get data from file and prepare list of dicts.
    Param: None.
    Return: List of dicts.
    """
    def preper_list(self):

        prepered_list_of_dicts = []
        nr_of_data_in_line = 0
        flag_0 = False
        datas = []

        try:
            with open(self.file_name, "r", encoding="utf8") as file_0:  # Open file in read mode.

                # Get data from file into "datas" list.
                for line in file_0:
                    datas.append(line.rsplit("="))

        except FileNotFoundError:
            print("File was not founded. It can be caused, because You don't have a learned words yet. Try first choose option to learn new words, insted repeting option.")
            return False, prepered_list_of_dicts
        except Exception:
            print("Problem was occur at attempt of open file.")
            return False, prepered_list_of_dicts

        if flag_0 is False:
            nr_of_data_in_line = len(datas[0])  # Get number of datas in one list inside "datas" list.
            flag_0 = True

        for word in datas:  # Loop through datas.
            d_of_words = {}  # Clear "d_of_words" dict.

            if nr_of_data_in_line == 3:  # If number of dates in one list is equal 3
                d_of_words["index"] = int(word[0])
                d_of_words["foreign word"] = word[1]
                d_of_words["native translation"] = word[2][:-1]
            elif nr_of_data_in_line == 5:  # If number of dates in one list is equal 3
                d_of_words["index"] = int(word[0])
                d_of_words["foreign word"] = word[1]
                d_of_words["native translation"] = word[2]
                d_of_words["number for repeat"] = int(word[3])
                d_of_words["date of repeat"] = word[4][:-1]
            else:
                print("Wrong number!")

            prepered_list_of_dicts.append(d_of_words)  # Append "d_of_words" dict into "prepered_list_of_dicts" list.

        return True, prepered_list_of_dicts  # After loop return finished list of dicts.
