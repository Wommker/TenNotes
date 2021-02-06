from tkinter import *
from io import open
import sqlite3, datetime, pickle
from datetime import date
from tkinter.font import Font

#Create database with the names of the notes and books
def create():
    try:
        myconnection=sqlite3.connect("BD")
        mycursor=myconnection.cursor()
        mycursor.execute("CREATE TABLE BOOKS (INI VARCHAR(500) UNIQUE, BOOK VARCHAR(500), NOTE VARCHAR(500))")
        myconnection.close()
        #
        myconnection=sqlite3.connect("BD")
        mycursor=myconnection.cursor()
        #
        for x in range(1,11):
            for i in range(1,11):
                BookNote = str(x) + " " + str(i)
                Book = "Book " + str(x) 
                Note = "Note " + str(i)
                mycursor.execute("INSERT INTO BOOKS VALUES('"+BookNote+"','"+Book+"','"+Note+"')")
        #
        archive=open("file","wb")
        archive.close
        myconnection.commit()
        myconnection.close()
    except:
        pass

#Rename buttons and notes and change the book that is selected
def botonbook(ID):
    #
    global Book
    Book = ID
    #
    myconnection=sqlite3.connect("BD")
    mycursor=myconnection.cursor()
    mycursor.execute("SELECT * FROM BOOKS ")
    bookmarkslist=mycursor.fetchall()
    #
    sbookone.set((bookmarkslist[0])[1])
    sbooktwo.set((bookmarkslist[10])[1])
    sbookthree.set((bookmarkslist[20])[1])
    sbookfour.set((bookmarkslist[30])[1])
    sbookfive.set((bookmarkslist[40])[1])
    sbooksix.set((bookmarkslist[50])[1])
    sbookseven.set((bookmarkslist[60])[1])
    sbookeight.set((bookmarkslist[70])[1])
    sbooknine.set((bookmarkslist[80])[1])
    sbookten.set((bookmarkslist[90])[1])
    #
    snoteone.set((bookmarkslist[int(str(ID)+"0")])[2])
    snotetwo.set((bookmarkslist[int(str(ID)+"1")])[2])
    snotethree.set((bookmarkslist[int(str(ID)+"2")])[2])
    snotefour.set((bookmarkslist[int(str(ID)+"3")])[2])
    snotefive.set((bookmarkslist[int(str(ID)+"4")])[2])
    snotesix.set((bookmarkslist[int(str(ID)+"5")])[2])
    snoteseven.set((bookmarkslist[int(str(ID)+"6")])[2])
    snoteeight.set((bookmarkslist[int(str(ID)+"7")])[2])
    snotenine.set((bookmarkslist[int(str(ID)+"8")])[2])
    snoteten.set((bookmarkslist[int(str(ID)+"9")])[2])
    #
    Pos()

#Change the selected note
def botonnote(ID):
    global Note
    Note = ID
    #
    Pos()

#Change the text in the Entry and If there is a saved note, insert it in the text
def Pos():
    textone.delete(1.0,END)
    found_start  = 0
    end_found = 0
    found = False
    #
    myconnection=sqlite3.connect("BD")
    mycursor=myconnection.cursor()
    mycursor.execute("SELECT * FROM BOOKS ")
    bookmarkslist=mycursor.fetchall()
    #
    snewbookname.set((bookmarkslist[int(str(Book)+"0")])[1])
    snewnotename.set((bookmarkslist[int(str(Book)+str(Note))])[2])
    #
    try:
        archiver=open("file","rb")
        file_list =pickle.load(archiver)
        for i in range(len(file_list)):
            if file_list[i] == ("----*O*----"+str(Book)+" " +str(Note)+"----*O*----"):
                found = True  
                found_start = i
            if file_list[i] == ("----*C*----"+str(Book)+" " +str(Note)+"----*C*----"):
                end_found = i
        if found:
            for i in range(found_start,end_found):
                if file_list[i] != ("----*O*----"+str(Book)+" " +str(Note)+"----*O*----"): 
                    textone.insert(END, file_list[i])
    except:
        pass

#If there is a secondary note insert it in the secondary text
def secondtext():
    try:
        archiver=open("file","rb")
        file_list=pickle.load(archiver)
        found=False
        for i in range(len(file_list)):
            if file_list[i] == ("----*O*----10 1----*O*----"):
                found = True  
                found_start = i
            if file_list[i] == ("----*C*----10 1----*C*----"):
                end_found = i
        print(found)
        if found:
            for i in range(found_start,end_found):
                if file_list[i] != ("----*O*----10 1----*O*----"):
                    texttwo.insert(END, file_list[i])
    except:
        pass


#Save name of books if they are changed
def SaveBook():
    myconnection=sqlite3.connect("BD")
    mycursor=myconnection.cursor()
    mycursor.execute("SELECT * FROM BOOKS ")
    bookmarkslist=mycursor.fetchall()
    #
    mycursor.execute("UPDATE BOOKS SET BOOK='"+snewbookname.get()+"' WHERE BOOK = '"+(bookmarkslist[int(str(Book)+"0")])[1]+"'")
    myconnection.commit()
    myconnection.close()
    botonbook(Book)

#Save name of notes if they are changed
def SaveNote():
    myconnection=sqlite3.connect("BD")
    mycursor=myconnection.cursor()
    mycursor.execute("SELECT * FROM BOOKS ")
    bookmarkslist=mycursor.fetchall()
    #
    mycursor.execute("UPDATE BOOKS SET NOTE='"+snewnotename.get()+"' WHERE INI = '"+str((bookmarkslist[int(str(Book)+str(Note))])[0])+"'")
    myconnection.commit()
    myconnection.close()
    botonbook(Book)

#Check if the database exists
def Save():
    try:
        archver=open("file","rb")
        file_list=pickle.load(archver)
        archver.close
        Saved(True, Book, Note, True)
    except:
        Saved(False, Book, Note, True)

#Save notes
def Saved(existe, Books, Notes,teksto):
    if teksto:
        text = textone.get("1.0",END)
    else:
        text = texttwo.get("1.0",END)
    #
    if existe:
        found = False
        found_start = 0
        end_found = 0
        #
        archiver=open("file","rb")
        file_list=pickle.load(archiver)
        archivew=open("file","wb")
        #
        for i in range(len(file_list)):
            if file_list[i] == ("----*O*----"+str(Books)+" " +str(Notes)+"----*O*----"):
                found = True 
                found_start = i
            if file_list[i] == ("----*C*----"+str(Books)+" " +str(Notes)+"----*C*----"):
                end_found = i
        #
        if found:
            for i in range(found_start,end_found):
                if file_list[i] != ("----*O*----"+str(Books)+" " +str(Notes)+"----*O*----"):
                    file_list.pop(i)
            file_list.insert(found_start+1,text)
        else:
            file_list.append("----*O*----"+str(Books)+" " +str(Notes)+"----*O*----")
            file_list.append(text)
            file_list.append("----*C*----"+str(Books)+" " +str(Notes)+"----*C*----")
        #
        pickle.dump(file_list,archivew)
        archivew.close()
        archiver.close()
    else:
        archivew=open("file","wb")
        file_list=["----*O*----"+str(Books)+" " +str(Notes)+"----*O*----",text,"----*C*----"+str(Books)+" " +str(Notes)+"----*C*----"]
        pickle.dump(file_list,archivew)

#Update time and save secondary text
def update():
    root.after(250,update)
    today = datetime.datetime.today()
    time.set(str(today.hour)+":"+str(today.minute)+":"+str(today.second))
    dates.set(str(today.day)+" - "+stringmonth.get())
    #
    try:
        archiver=open("file","rb")
        file_list=pickle.load(archiver)
        archiver.close
        Saved(True, 10, 1, False)
    except:
        Saved(False, 10, 1, False)

#Interface
root= Tk()
root.resizable(False,False)
root.title("Notes")
#
frame=Frame(root)
frame.config(bg="#222222")
frame.pack()
#Time variables
today = datetime.datetime.today()
myFont =Font(family="Times New Roman", size=18)
dates = StringVar()
stringmonth = StringVar()

if today.month == 1:
    stringmonth.set("January")
elif today.month == 2:
    stringmonth.set("February")
elif today.month == 3:
    stringmonth.set("March")
elif today.month == 4:
    stringmonth.set("April")
elif today.month == 5:
    stringmonth.set("May")
elif today.month == 6:
    stringmonth.set("June")
elif today.month == 7:
    stringmonth.set("July")
elif today.month == 8:
    stringmonth.set("August")
elif today.month == 9:
    stringmonth.set("September")
elif today.month == 10:
    stringmonth.set("October")
elif today.month == 11:
    stringmonth.set("November")
elif today.month == 12:
    stringmonth.set("December")


dates.set(str(today.day)+" - "+stringmonth.get())
year = str(today.year)
#
entry_date=Label(frame, textvariable=dates)
entry_date.config(bg="#222222",fg="#008722", font=myFont)
entry_date.grid(row=0, column=0, sticky="w", padx=10,pady=10)
#
time = StringVar()
time.set(str(today.hour)+":"+str(today.minute)+":"+str(today.second))
#
entry_time=Label(frame, textvariable=time)
entry_time.config(bg="#222222",fg="#008722", font=myFont)
entry_time.grid(row=0, column=1, sticky="w", padx=10,pady=10)
#
timetoendtoday= date(today.year,today.month,today.day)
timetoendend= date(today.year, 12, 31)
delta = StringVar()
delta.set((timetoendend-timetoendtoday).days)
entry_datea=Label(frame, textvariable=delta)
entry_datea.config(bg="#222222",fg="#008722", font=myFont)
entry_datea.grid(row=0, column=2, sticky="w", padx=10,pady=10)
#
sbookone = StringVar()
sbooktwo = StringVar()
sbookthree = StringVar()
sbookfour = StringVar()
sbookfive = StringVar()
sbooksix = StringVar()
sbookseven = StringVar()
sbookeight = StringVar()
sbooknine = StringVar()
sbookten = StringVar()
#
snoteone = StringVar()
snotetwo = StringVar()
snotethree = StringVar()
snotefour = StringVar()
snotefive = StringVar()
snotesix = StringVar()
snoteseven = StringVar()
snoteeight = StringVar()
snotenine = StringVar()
snoteten = StringVar()
#
Book = 0
Note = 0

#Buttons for books
buttononebook=Button(frame, textvariable=sbookone, command=lambda:botonbook(0))
buttononebook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttononebook.grid(row=11, column=1, sticky="w", padx=5)
#
buttontwobook=Button(frame, textvariable=sbooktwo, command=lambda:botonbook(1))
buttontwobook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttontwobook.grid(row=12, column=1, sticky="w", padx=5)
#
buttonthreebook=Button(frame, textvariable=sbookthree, command=lambda:botonbook(2))
buttonthreebook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonthreebook.grid(row=13, column=1, sticky="w", padx=5)
#
buttonfourbook=Button(frame, textvariable=sbookfour, command=lambda:botonbook(3))
buttonfourbook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonfourbook.grid(row=14, column=1, sticky="w", padx=5)
#
buttonfivebook=Button(frame, textvariable=sbookfive, command=lambda:botonbook(4))
buttonfivebook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonfivebook.grid(row=15, column=1, sticky="w", padx=5)
#
buttonsixbook=Button(frame, textvariable=sbooksix, command=lambda:botonbook(5))
buttonsixbook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonsixbook.grid(row=16, column=1, sticky="w", padx=5)
#
buttonsevenbook=Button(frame, textvariable=sbookseven, command=lambda:botonbook(6))
buttonsevenbook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonsevenbook.grid(row=17, column=1, sticky="w", padx=5)
#
buttoneightbook=Button(frame, textvariable=sbookeight, command=lambda:botonbook(7))
buttoneightbook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttoneightbook.grid(row=18, column=1, sticky="w", padx=5)
#
buttonninebook=Button(frame, textvariable=sbooknine, command=lambda:botonbook(8))
buttonninebook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonninebook.grid(row=19, column=1, sticky="w", padx=5)
#
buttontenbook=Button(frame, textvariable=sbookten, command=lambda:botonbook(9))
buttontenbook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttontenbook.grid(row=20, column=1, sticky="w", padx=5)

#Buttons for notes
buttononenote=Button(frame, textvariable=snoteone, command=lambda:botonnote(0))
buttononenote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttononenote.grid(row=1,column=2,sticky="w", padx=10, pady=5,columnspan = 2)
#
buttontwonote=Button(frame, textvariable=snotetwo, command=lambda:botonnote(1))
buttontwonote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttontwonote.grid(row=2,column=2,sticky="w", padx=10, pady=5,columnspan = 2)
#
buttonthreenote=Button(frame, textvariable=snotethree, command=lambda:botonnote(2))
buttonthreenote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonthreenote.grid(row=3,column=2,sticky="w", padx=10, pady=5,columnspan = 2)
#
buttonfournote=Button(frame, textvariable=snotefour, command=lambda:botonnote(3))
buttonfournote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonfournote.grid(row=4,column=2,sticky="w", padx=10, pady=5,columnspan = 2)
#
buttonfivenote=Button(frame, textvariable=snotefive, command=lambda:botonnote(4))
buttonfivenote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonfivenote.grid(row=5,column=2,sticky="w", padx=10, pady=5,columnspan = 2)
#
buttonsixnote=Button(frame, textvariable=snotesix, command=lambda:botonnote(5))
buttonsixnote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonsixnote.grid(row=6,column=2,sticky="w", padx=10, pady=5,columnspan=  2)
#
buttonsevennote=Button(frame, textvariable=snoteseven, command=lambda:botonnote(6))
buttonsevennote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonsevennote.grid(row=7,column=2,sticky="w", padx=10, pady=5,columnspan=  2)
#
buttoneightnote=Button(frame, textvariable=snoteeight, command=lambda:botonnote(7))
buttoneightnote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttoneightnote.grid(row=8,column=2,sticky="w", padx=10, pady=5,columnspan=  2)
#
buttonninenote=Button(frame, textvariable=snotenine, command=lambda:botonnote(8))
buttonninenote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonninenote.grid(row=9,column=2,sticky="w", padx=10, pady=5,columnspan=  2)
#
buttontennote=Button(frame, textvariable=snoteten, command=lambda:botonnote(9))
buttontennote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttontennote.grid(row=10,column=2,sticky="w", padx=10, pady=5,columnspan=  2)

#Edit the book name
buttoneditbook=Label(frame, text="Book: ")
buttoneditbook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttoneditbook.grid(row=11, column=2, sticky="w", padx=5)

snewbookname=StringVar()

entrynewbook=Entry(frame, textvariable=snewbookname, bg="#222222",fg="#008722", bd = 2)
entrynewbook.grid(row=11, column = 3,padx=5)

buttonsavenewbook=Button(frame, text="Save Book", command=lambda:SaveBook())
buttonsavenewbook.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonsavenewbook.grid(row=12, column=3, sticky="w", padx=5)

#Edit the note name
buttoneditnote=Label(frame, text="Note: ")
buttoneditnote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttoneditnote.grid(row=13, column=2, sticky="w", padx=5)

snewnotename=StringVar()

entrynewnote=Entry(frame, textvariable=snewnotename, bg="#222222",fg="#008722", bd = 2)
entrynewnote.grid(row=13, column = 3,padx=5)

buttonsavenewnote=Button(frame, text="Save Note", command=SaveNote)
buttonsavenewnote.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
buttonsavenewnote.grid(row=14, column=3, sticky="w", padx=5)

#Texts
textone=Text(frame)
textone.config(font="Fixedsys", bg= "#000000", fg="#008722", bd = 0, insertbackground= "#008722", insertwidth=4,wrap=WORD,)
textone.grid(row=1,column=0,columnspan = 2,rowspan=10)

texttwo=Text(frame, width=30, height=15)
texttwo.config(font="Fixedsys", bg= "#222222", fg="#008722", bd = 1, insertofftime=1, insertontime=0,insertwidth=4,wrap=WORD,cursor="arrow")
texttwo.grid(row=11,column=0,rowspan=10)

#Save text
savetext=Button(frame, text="Save", command=Save)
savetext.config(bg="#222222",fg="#008722",bd = 0,activeforeground="red",activebackground="#222222")
savetext.grid(row=15, column=3, sticky="w", padx=5)

#Call functions
secondtext()
update()
create()
botonbook(Book)
root= mainloop()