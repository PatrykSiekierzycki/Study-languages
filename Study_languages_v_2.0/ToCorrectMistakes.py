import Dates

"""
Brief: Class responsible for operation at words with incorrect user's answers.
"""
class ToCorrectMistakes:

    """"
    Brief: Get list of dicts to correct.
    Param: List of dicts
    Return: None. __init__ method can't return a value.
    """
    def __init__(self, mistakes):
        self.mistakes = mistakes

    """
    Brief: Method responsible for correct the mistakes.
    Param: None.
    Return: None.
    """
    def again(self):
        lenght = len(self.mistakes)  # Get a number of elements into "mistakes" list.

        # Checking mechanism
        while 0 < lenght:  # Unitll "mistakes" list isn't empty.
            lenght = len(self.mistakes)  # Check lenght of "mistakes" list.

            for x in self.mistakes:  # Loop through "mistakes" list.

                answer = input(x["native translation"] + ": ")  # Get answer from user.

                # Get back repeats
                x["number for repeat"] = 0  # Set "number for repeat" to 0.
                date_object = Dates.Dates()  # Create a "Dates.Dates" object.
                rep_date = date_object.calculate_date_for_next_repeat(x["number for repeat"])  # Get date of next repeat.
                x["date of repeat"] = rep_date  # Put that date inside word's dictionary.

                # Check user answer
                if x["foreign word"] == answer:  # If user's answer is correct.
                    self.mistakes.remove(x)  # If user's answer is correct, remove that word from "mistakes" list.
                    print("Correct")
                else:  # If User's answer is incorrect.
                    print("Incorect: " + x["foreign word"])
