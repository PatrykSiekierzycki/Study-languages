import os.path


class Give_indexes:

    def __init__(self, file_name):

        i = 0
        lines = []

        with open(file_name, "r", encoding="utf8") as file_0:  # Open file

            for line in file_0:  # Go through all file and add index for each line.
                i += 1
                line = str(i) + "=" + line
                lines.append(line)

        for line in lines:  # Print efect
            print(line)

        # Ask user if he want to save changes
        chooise = input("Do you want to  save data (y/n)")
        if chooise != "y":
            input("Data wasn't save in file.")
            exit(0)

        # Save changes
        with open(file_name, "w", encoding="utf8") as file_1:
            for line in lines:
                file_1.write(line)


path_to_file = input("Give path to the file, you want add indexes: ")  # Ask user for path to dictionary file.

if os.path.exists(path_to_file) is False:
    path_to_file = input("Wrong path try again: ")

object_g_i = Give_indexes(path_to_file)
