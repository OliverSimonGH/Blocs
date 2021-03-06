import os
from flask import Flask, redirect, request, render_template
import sqlite3

DATABASE = 'blocs.db'

def create_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS Blocs (\
    `Title` TEXT NOT NULL,\
    `Description` TEXT NOT NULL,\
    `Link` TEXT NOT NULL);')
    conn.close()

def populate_tables():
    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO Blocs (`Title`,`Description`, `Link`) VALUES('First bloc', 'Second bloc', 'This is a description');")
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
    print(cur.fetchall())
    conn.close()

def write_bloc_to_database(parameters):
    print("Called")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO Blocs(`Title`, `Description`, `Link`) VALUES(?, ?, ?)", parameters)
    conn.commit()
    conn.close()
