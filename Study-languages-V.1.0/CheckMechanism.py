import os

import Dates, ToCorrectMistakes, LoadFiles, time


""""
Brief: Class responsible for handling checking user's answers.
"""
class Check_mechanism:

    points = 0  # Points for good answer.
    mistakes = []  # List of dicts to correct.

    def __init__(self, username, list_of_words_to_work, files_list, language):
        self.username = username  # Login usera.
        self.list_of_words_to_work = list_of_words_to_work  # List of dicts to work (unlearned words/words to repeat)
        self.files_list = files_list  # List of names for user's file.
        self.language = language - 1  # Number to describe option (1. English-Polish, 2. Japanese-Polish, 3. Romanian-Polish)
        self.file_name = "users/" + self.username + "/" + self.files_list[self.language]  # Path to choosed user's file.

    """
    Brief: Check if user give good answers for new learned words, then save new learned words inside user's file.
    Param: None.
    Return: None.
    """
    def check_mechanism_for_new_words(self):
        flag_1 = False
        lenght = len(self.list_of_words_to_work)  # How many words to work.
        how_many_words = 0  # How many words user's want to work.

        # Protection before to big number from user
        while flag_1 is False:
            how_many_words = int(input("Give the number of words to train: "))

            if lenght >= how_many_words and how_many_words > 0:
                flag_1 = True
            else:
                print("Error 1: Not enough word in dictionary or number are below zero. Choose smaller number of words to train.")
                flag_1 = False

        # Show foreign and native words
        i = 0
        while i < how_many_words:
            print(self.list_of_words_to_work[i]["foreign word"] + ": ")
            time.sleep(5)
            print(self.list_of_words_to_work[i]["native translation"])
            i += 1

        go_further = input("If you ready, tap any key! ")  # Ask user is he ready to train words.

        os.system("cls")

        # Ask user for answer, check it and save date for repeat
        date_object = Dates.Dates()  # Create "Dates.Dates" object.
        i = 0
        while i < how_many_words:  # Untill all words will be finished
            answer = input(self.list_of_words_to_work[i]["native translation"] + ": ")  # Get user's answer
            # Check mechanism
            if self.list_of_words_to_work[i]["foreign word"] == answer:  # If answer is correct
                print("Correct")
                self.points += 1  # Increase user's point.
                self.list_of_words_to_work[i]["number for repeat"] = 0  # Add to word list new key and set value to 0.
                self.list_of_words_to_work[i]["date of repeat"] = date_object.calculate_date_for_next_repeat(0)  # Calculate a date of next repeat and return it to new added key to word dictionary, and set as its value.
            else:  # If answer isn't correct.
                print("Incorect: " + self.list_of_words_to_work[i]["foreign word"])
                self.list_of_words_to_work[i]["number for repeat"] = 0  # Add to word list new key and set value to 0.
                self.list_of_words_to_work[i]["date of repeat"] = date_object.calculate_date_for_next_repeat(0)  # Calculate a date of next repeat and return it to new added key to word dictionary, and set as its value.
                self.mistakes.append(self.list_of_words_to_work[i])  # Append dict of word to "mistakes" list.

            # Save learned words inside file
            with open(self.file_name, "a+", encoding="utf8") as file_1:
                file_1.write(str(self.list_of_words_to_work[i]["index"]) + "=" + self.list_of_words_to_work[i]["foreign word"] + "=" + self.list_of_words_to_work[i]["native translation"] + "=" + str(self.list_of_words_to_work[i]["number for repeat"]) + "=" + str(self.list_of_words_to_work[i]["date of repeat"]) + "\n")
            i += 1

        # Print score.
        print("Correct answers: " + str(self.points) + "\n")
        print("Percentage of correct answer: " + str(round(self.points/how_many_words * 100, 2)) + "%")

        # Correct mistakes.
        ToCorrectMistakes_object = ToCorrectMistakes.ToCorrectMistakes(self.mistakes)
        ToCorrectMistakes_object.again()

    """
    Brief: Check if user correct repeat word. Next update data of repeated words and save into user's file.
    Param: None.
    Return: None or 0 if there is no words to repeat.
    """
    def check_mechanism_for_repeats(self):
        i = 0
        flag_1 = False
        lenght = len(self.list_of_words_to_work)
        how_many_words = 0
        date_object = Dates.Dates()

        # Get list of all words from users file
        object_Get_list_of_dicts = LoadFiles.Get_list_of_dicts(self.files_list[self.language])
        full_list_of_words = object_Get_list_of_dicts.preper_list()
        lenght_of_users_file = len(full_list_of_words)
        print("Number of words to repeat: ", lenght)

        # Protection before sytuation, when there is no words to repeat.
        if not lenght:
            print("There is no words to repeat.")
            return 0

        # Protection before to big number from user.
        while flag_1 is False:
            how_many_words = int(input("Give the number of words to train: "))

            if lenght >= how_many_words and how_many_words > 0:
                flag_1 = True
            else:
                print("Error 1: Not enough word in dictionary or number are below zero. Choose smaller number of words to train.")
                flag_1 = False

        # Ask user for answer, check it and save date for repeat
        while i < how_many_words:

            answer = input(self.list_of_words_to_work[i]["native translation"] + ": ")  # Get user's answer

            # Check mechanism
            if self.list_of_words_to_work[i]["foreign word"] == answer:
                print("Correct")
                self.points += 1  # Add points.
                if self.list_of_words_to_work[i]["number for repeat"] < 6:  # Protection before end of list with number of days for next day repeat.
                    self.list_of_words_to_work[i]["number for repeat"] += 1  # Increment "number for repeat"
                self.list_of_words_to_work[i]["date of repeat"] = date_object.calculate_date_for_next_repeat(self.list_of_words_to_work[i]["number for repeat"])  # Get data of next repeat.
            else:
                print("Incorect: " + self.list_of_words_to_work[i]["foreign word"])
                self.list_of_words_to_work[i]["number for repeat"] = 0  # Return value of "number for repeats" to zero.
                self.list_of_words_to_work[i]["date of repeat"] = date_object.calculate_date_for_next_repeat(0)  # Get data of next repeat.
                self.mistakes.append(self.list_of_words_to_work[i])  # Append word dicts to "mistakes" list.
            i += 1

        # Put indexes of words to repeat inside "list_of_indexes_of_words_to_work" list.
        list_of_indexes_of_words_to_work = []  # List for indexes of words to repeat.
        for diction in self.list_of_words_to_work:
            list_of_indexes_of_words_to_work.append(diction["index"])

        finished_list = []
        x = 0
        while x < lenght_of_users_file:  # Untill "x" is lesser than number of line for each word inside user's file.

            if full_list_of_words[x]["index"] in list_of_indexes_of_words_to_work:  # If index of word from file is inside "list_of_indexes_of_words_to_work" list
                for line in self.list_of_words_to_work:  # Loop through "self.list_of_words_to_work" list
                    if line["index"] == full_list_of_words[x]["index"]:  # If index of word from "self.list_of_words_to_work" list is the same as index of actual "looping" word from "full_list_of_words" list
                        finished_list.append(line)  # Append that dict to "finished_list".
                    elif type(line) == int:  # Protection by empty line at end of the file.
                        break
            else:  # If index of word from "self.list_of_words_to_work" list is not the same as index of actual "looping" word from "full_list_of_words" list
                finished_list.append(full_list_of_words[x])  # Add actual "looping" dict from "full_list_of_words".
            x += 1

        if how_many_words > 0:  # Protection before removeing all date from file
            # Save learned words inside file
            with open(self.files_list[self.language], "w", encoding="utf8") as file_1:
                z = 0
                while z < lenght_of_users_file:
                    file_1.write(str(finished_list[z]["index"]) + "=" + finished_list[z]["foreign word"] + "=" +
                                 finished_list[z]["native translation"] + "=" + str(
                        finished_list[z]["number for repeat"]) + "=" + str(finished_list[z]["date of repeat"]) + "\n")
                    z += 1

        # Display score
        print("Correct answers: " + str(self.points) + "\n")
        print("Percentage of correct answer: " + str(round(self.points/how_many_words * 100, 2)) + "%")

        # Repeat wrong words
        if len(self.mistakes):  # If "self.mistakes" list isn't empty
            ToCorrectMistakes_object = ToCorrectMistakes.ToCorrectMistakes(self.mistakes)
            ToCorrectMistakes_object.again()
