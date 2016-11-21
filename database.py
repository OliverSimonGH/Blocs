import os
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = 'Blocs.db'

def create_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS Blocs (\
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
    `Title` TEXT NOT NULL,\
    `Description` TEXT NOT NULL,\
    `Link` TEXT NOT NULL, \
    `TagID` INTEGER NOT NULL,\
    FOREIGN KEY(TagID) REFERENCES Tags(ID));')
    conn.close()

def create_tags():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS Tags (\
    `ID` INTEGER PRIMARY KEY NOT NULL, \
    `Title` TEXT NOT NULL);')
    conn.close()

def populate_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO Tags (`Title`) VALUES('All')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('Video')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('Web')")
    conn.execute("INSERT INTO Tags (`Title`) VALUES('Images')")
    conn.execute("INSERT INTO Tags ( `Title`) VALUES('Favourites')")
    conn.commit()
    conn.close()

def delete_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute("DROP TABLE IF EXISTS Blocs;")
    conn.commit()
    conn.close()

def select_all():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Blocs")
    conn.row_factory = sqlite3.Row
    result = cur.fetchall()
    conn.close()
    return result

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
