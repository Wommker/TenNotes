# TenNotes

It is a note organizer, which allows you to have 10 notes contained in each book, by having 10 books you have a total of 100 possible notes. Try to make Evernote work, that is, you could create as many books as the user wanted and in each book place as many notes as the user wants, in addition to different presets to help in their use. However, my current knowledge is much less than what could be needed for it.

Looking at another way, the program is very simple but functional, it allows you to save 100 notes without being too complex, it has a date-time marker and how many days are left to finish the year, and it also allows you to change the name of any book and note, for The last one has a section where you can write a note that will be saved automatically every 250 milliseconds, this has the objective of serving as a reference table, that is, it shows you what you want to write when starting the program, it is perfect for reminders, list of things to do or messages to yourself.

At the programming level it does not have OOP and makes a lot of use of the "for" loop to move through the list that contains all the saved notes, each one classified with an index called "INI" that has two numbers, the first indicates the number of the book and the second the number of the note. It also has 5 "try" to avoid errors if it does not find files such as the database where the names of books and notes are stored or if it does not find the file in binary with the saved notes. To add something else, the code is separated by comments, some that describe the section of the code and others that only separate it into parts.

Used libraries:
• tkinter
• io
• sqlite3
• datetime
• pickle

If you have any opinion, doubt or any rational thought that has as its root I wrote it in this small post, do not hesitate to write it.
