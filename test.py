import psycopg2
from psycopg2 import OperationalError
import tkinter
from tkinter import *
from tkinter import Tk, Checkbutton, Button, Menu, Entry, BooleanVar, Toplevel
from tkinter.ttk import Label, Combobox, Treeview
from bd import Datebase
import bd_commands

def create_connection(db_name, db_user, db_password, db_host, db_port):
    # функция подключения к бд postgrsql
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


con = Datebase("store", "postgres", "585303", "127.0.0.1", "2669")
#connection = create_connection("store", "postgres", "29103939", "127.0.0.1", "2669")
con.get_all_table('wide_group')
print(con)