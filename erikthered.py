#!/usr/env/python
import os
import sys
import dns
# import nmap
import pyfiglet
import sqlite3


## Variables
nm = nm.PortScanner()
banner = pyfiglet.figlet_format('ErikTheRed')
usage_text = '''

'''


def main_menu():
    os.system('clear')
    print(banner)
    print()
    print ("Main Menu:")
    print ("         1. Create new session")
    print ("         2. Open existing session")
    print ("         3. Use for single session")
    print ("         4. Exit ErikTheRed")
    function = int(input("Please choose a function: "))
    if function == 1:
        db_name = str(input('DB name to create?'))
        create_db_file(db_name)
        return True
    elif function == 2:
        db_name = str(input('Please type the name of the session you''d like to open:'))
        open_db_file(db_name)
        return True
    elif function == 3:
        print ('Opening session in memory')
        create_db_mem()
        return True
    elif function == 4:
        print ("Thanks for using ErikTheRed. Happy pilaging!.")
        sys.exit()
    else:
        print ("Unknown option.")
    return False

def create_db_file(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_db_mem():
    """ create a database connection to a database that resides
        in the memory
    """
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == "__main__":
    main_menu()
    exit