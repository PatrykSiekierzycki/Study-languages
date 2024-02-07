Program for study languages:

Version: 1.0

What the program offer:
1. Creat a your personal accout.
2. Learn new words from 3 other languages: english, japanese (roumaji), romanian (program presume you know polish).
3. Save your words for each available language.
4. Offer repeat option.
5. Show simple statistics (How many words are correct, and percentage of correct answers).
6. You don't need a internet access. Everything is localy on your computer.

- Program work into command line.
- It is necessery to creat accout.
- Created acount is only on your computer. Data are't send to any database.
- Created accout help in sytuation if on one computer are more than one person.
- Login datas aren't encrypted.
- Program provide option to study words for 3 languages: english, japanese (roumaji), romanian (program presume you know polish).
- A basic language is polish.
- Program offer an option for repeat already learned words. After choosing language, choose option for repeat.
All learned word will be automatically checked if should be repeated or not.
If should be repeated, then will be displed a option to choose how many word you want to repeat.
Repeated will be only proper words, and only for choosed languages.

How programs are build:
1. Log in or sign up
2. Choose language
3. Choose Learn new words or do repeat.
5. Give correct answers for all mistakes.
4. Program save data and quit.

Note: If you make mistake untill learning or repeating, program will be want you to give a corrent answer.

About repeats option:
1. If you learned new word, the word will be automatically added to your personal file for choosed languages, and will be added two new information:
- numebr of repeat - is responsible for tell the program, for how many days will be next repeat (bigger number - more days)
- date of new repeat
2. If during repeats you make mistake, number of repeat will be change to 0, and date of next repeat will be nearest.
3. If during repeats you don't make mistake the number od repeat will be increment, and date of next repeat will be further in future.
4. If you miss repeats, then that repeat will be added for your next repeat session.

About python's files:
1. main.py - just run file Menu.py.
2. Menu.py - handle login and registration and run file LoadFiles.py.
3. LoadFiles.py - get information from user about what he want, prepere data for operations and run file CheckMechanism.py.
4. CheckMechanism.py - handle users answers, checking it, display stats, eventually run file ToCorrectMistakes.py,. Also use file Dates.py.
5. To CorrectMistakes.py - handle "forcing" user for correct answers for each mistakes.
6. Datas.py - handle working with dates. Calculate date for next repeat, and check words if should be repeated.
7. Give indexes.py - it is a extra file. Handle giving indexes for each words, if data in file looks like (foreign_word=native_word) for each row (one word with translation per line in file).
Result will be looks like (index=foreign_word=native_word) for each line in file.

About other files:
- Each dictionary file in catalogue call "dictionaries files" has structure (index=foreign_word=native_word). Data for all words has it's own line.
- Each user's file in catalogue call the same as user login, contain date about already learned user's words and has structure (index=foreign_word=native_word=number_of_repeat=date_of_repeat). Data for all words has it's own line.
- File into catalogue "users" call "users_database.txt" contain login's data for each user and has structure (index=login=native_language=password). One line for one user.

Note: As you can see, I use as separator for data sign "=". It is because some native words or foreign word can contain specific character, for example: (-, ;, :).
______________________________________________________________________________________

Version: 2.0

Version 2.0 contain everything from version 1.0 and added options.

Changelog:
	1. Get rid of bugs from version 1.0.
	2. More protected files openings.
	3. Password is now hashed.
	4. Zip file contain instalator and .exe file for run program.

How install the program:
	1. At github website, look above there will be green button with text "Code". Click it. When you do this, you will see a context menu. Choose option "Download ZIP folder".
	2. When you click it, the .zip folder will be downloaded on your local computer. Open it and click "Installator".
	3. Follow by installator.
	4. After installation, go to the installed folder and click "Study Languages.exe".
	5. This will run a program.