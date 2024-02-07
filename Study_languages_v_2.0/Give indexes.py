import os.path


class Give_indexes:

    def __init__(self, file_name):

        i = 0
        lines = []
        try:
            with open(file_name, "r", encoding="utf8") as file_0:  # Open file

                for line in file_0:  # Go through all file and add index for each line.
                    i += 1
                    line = str(i) + "=" + line
                    lines.append(line)

        except FileNotFoundError:
            print("File was not founded.")
            exit(1)
        except Exception:
            print("Problem was occur at attempt of open file.")
            exit(1)

        for line in lines:  # Print efect
            print(line)

        # Ask user if he want to save changes
        chooise = input("Do you want to  save data (y/n)")
        if chooise != "y":
            input("Data wasn't save in file.")
            exit(0)

        # Save changes
        try:
            with open(file_name, "w", encoding="utf8") as file_1:
                for line in lines:
                    file_1.write(line)

        except FileNotFoundError:
            print("File was not founded.")
            exit(1)
        except Exception:
            print("Problem was occur at attempt of open file.")
            exit(1)


if __name__ == "__main__":
    path_to_file = input("Give path to the file, you want add indexes: ")  # Ask user for path to dictionary file.

    if os.path.exists(path_to_file) is False:
        path_to_file = input("Wrong path try again: ")

    object_g_i = Give_indexes(path_to_file)
