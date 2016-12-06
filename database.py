import os
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = 'blocs.db'

def create_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute("CREATE TABLE IF NOT EXISTS `Emails` (\
    `emailId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
    `emailAddress` TEXT NOT NULL UNIQUE,\
    `emailList` INTEGER);")

    conn.execute("CREATE TABLE IF NOT EXISTS `Blocs` (\
    `blocid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
    `weburl` TEXT NOT NULL,\
    `imgurl` TEXT NOT NULL,\
    `title` TEXT NOT NULL, \
    `notes` TEXT NOT NULL,\
    `category` TEXT NOT NULL,\
    `favourite` INTEGER NOT NULL);")
    # `TagID` INTEGER NOT NULL,\
    # FOREIGN KEY(TagID) REFERENCES Tags(ID));')

    conn.execute("CREATE TABLE IF NOT EXISTS `Logs` (\
    `logId` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
    `emailAddress` TEXT,\
    `sender` TEXT,\
    `date` TEXT,\
    `time` TEXT,\
    `blocList` TEXT);")

    conn.execute("CREATE TABLE IF NOT EXISTS `Users` (\
    `userid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
    `emailAddress` TEXT NOT NULL,\
    `password` TEXT NOT NULL);")

    conn.execute("CREATE TABLE IF NOT EXISTS `UserProfile` (\
    `profileid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
    `name` TEXT,\
    `qualifications` TEXT,\
    `emailAddress` TEXT,\
    `website` TEXT,\
    'twitter' TEXT,\
    'google' TEXT,\
    'facebook' TEXT);")
    conn.commit()
    conn.close()

def create_tags():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS Tags (\
    `ID` INTEGER PRIMARY KEY NOT NULL, \
    `Title` TEXT NOT NULL);')
    conn.close()

def populate_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO Blocs (`weburl`, `imgurl`, `title`, `notes`, `category`, `favourite`) VALUES('https://en-gb.facebook.com/', 'https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg', 'Facebook', 'Click this link to go to facebook', 'web', '1')")
    conn.execute("INSERT INTO Blocs (`weburl`, `imgurl`, `title`, `notes`, `category`, `favourite`) VALUES('https://taiga.cs.cf.ac.uk/', 'https://files.graphiq.com/stories/t2/tiny_cat_12573_8950.jpg', 'This is taiga', 'This link will take the user to taiga', 'images', '0')")
    conn.execute("INSERT INTO Blocs (`weburl`, `imgurl`, `title`, `notes`, `category`, `favourite`) VALUES('https://sqlite.org/lang.html', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkoIe-ZUjPzuxhO_TceItomnQ1CrLa2TpIU2TSC_MgaFdUgxxbfg', 'SQLite3', 'Learn how to code with SQLite3', 'video', '1')")
    conn.execute("INSERT INTO Blocs ( `weburl`, `imgurl`, `title`, `notes`, `category`, `favourite`) VALUES('https://intranet.cardiff.ac.uk/students', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdolGLviByI1PEjzD8jQfDwYRURYRSxwOWeUgLTHoYWP79ezXW', 'Cardiff Intranet', 'Explore multiple student options', 'video', '0')")
    conn.execute("INSERT INTO Blocs (`weburl`, `imgurl`, `title`, `notes`, `category`, `favourite`) VALUES('https://www.youtube.com/watch?v=rJAPZFE4C7I', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQQZ6m0ZmN6HNTQ2QYtdNZ0w6zidyGrL-YwZWlFAZ_KtMoqo4vT', 'Youtube sqlite', 'How to do email validation in flask', 'video', '1')")
    conn.execute("INSERT INTO Blocs (`weburl`, `imgurl`, `title`, `notes`, `category`, `favourite`) VALUES('https://css-tricks.com/snippets/jquery/make-entire-div-clickable/', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTym_yzPMS5O1LC9LTqvLvXjWmK-jiClSPHxxhRydciTj2SbJXD', 'CSS Tricks', 'Learn how to use CSS today', 'web', '0')")
    conn.execute("INSERT INTO Blocs (`weburl`, `imgurl`, `title`, `notes`,  `category`, `favourite`) VALUES('http://stackoverflow.com/questions/4858047/the-following-untracked-working-tree-files-would-be-overwritten-by-checkout', 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcThtVuIQ7CBYssbdwtzZjVLI_uw09SeLmyrxaRQEngnQAked5ZB', 'Stackoverflow problem - resolved', 'This link will help the user solve their problem with the link they are given', 'images', '1')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('All')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('Video')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('Web')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('Images')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('Favourites')")
    conn.execute("INSERT INTO Emails (`emailAddress`, 'emailList') VALUES('oliver@hotmail.co.uk', '1')")
    conn.execute("INSERT INTO Emails (`emailAddress`, 'emailList') VALUES('example@hotmail.co.uk', '1')")
    conn.execute("INSERT INTO Emails (`emailAddress`, 'emailList') VALUES('example1@hotmail.co.uk', '1')")
    conn.execute("INSERT INTO Emails (`emailAddress`, 'emailList') VALUES('example2@hotmail.co.uk', '1')")
    conn.execute("INSERT INTO Emails (`emailAddress`, 'emailList') VALUES('jake@yahoo.com', '1')")
    conn.execute("INSERT INTO Emails (`emailAddress`, 'emailList') VALUES('jake1@yahoo.com', '0')")
    conn.execute("INSERT INTO Emails (`emailAddress`, 'emailList') VALUES('jake2@yahoo.com', '0')")
    conn.execute("INSERT INTO Logs (`emailAddress`, `sender`, `date`, `time`) VALUES('alexandergmiles@hotmail.com', 'target@hotmail.com', '05/12/2016', '20:08')")
    conn.commit()
    conn.close()

def delete_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute("DROP TABLE IF EXISTS Blocs;")
    conn.execute("DROP TABLE IF EXISTS Emails;")
    conn.execute("DROP TABLE IF EXISTS Logs;")
    conn.execute("DROP TABLE IF EXISTS Users;")
    conn.execute("DROP TABLE IF EXISTS UserProfile;")
    conn.execute("DROP TABLE IF EXISTS Emails;")
    conn.commit()
    conn.close()

def select_all():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Blocs")
    conn.row_factory = sqlite3.Row
    result = cur.fetchall()
    #print(result)
    conn.close()
    return result

def update_table(parameters):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("UPDATE Blocs SET Title=?, Description=?, Link=? WHERE ID=?", (parameters[0], parameters[1], parameters[2], parameters[3]))
    conn.commit()
    conn.close()


def write_bloc_to_database(parameters):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    tag_value = check_param_value(parameters[3])
    cur.execute("INSERT INTO Blocs(`Title`, `Description`, `Link`, `TagID`) VALUES(?, ?, ?, ?)", (parameters[0], parameters[1], parameters[2], tag_value))
    conn.commit()
    conn.close()

def check_param_value(parameter):
    if parameter == "all":
        return 1
    elif parameter == "video":
        return 2
    elif parameter == "web":
        return 3
    elif parameter == "images":
        return 4
    elif parameter == "favourites":
        return 5

def create_email(email_sent, check):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO Emails (`emailAddress`, `emailList`) VALUES (?,?)", (email_sent, check))
    conn.commit()
    conn.close()

def write_log(parameters):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO Logs (`emailAddress`, `sender`, `date`, `time`, `blocList`) VALUES(?,?,?,?,?)", (parameters[0], parameters[1], parameters[2], parameters[3], parameters[4]))
    conn.commit()
    conn.close()

def read_logs():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Logs")
    conn.row_factory = sqlite3.Row
    result = cur.fetchall()
    conn.close()
    return result

def create_user(email, password):
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO Users (`emailAddress`, `password`) VALUES(?,?)", (email, password))
        conn.commit()
        conn.close()
        return true
    except Exception as e:
        return false
