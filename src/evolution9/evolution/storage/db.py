'''
Created on Oct 11, 2010

@author: cagatay.yuksel
'''

from evolution9.constants import SQLITE_FILE
import sqlite3

def initDatabase():
    connection = sqlite3.connect(SQLITE_FILE)
    c = connection.cursor()

    # Create table
    c.execute('''
            create table if not exists composers(
                        generation integer, 
                        gene text, 
                        status text)
            ''')
    c.close()
    connection.close()
