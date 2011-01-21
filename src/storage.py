'''
Created on Oct 11, 2010

@author: melih.karci
'''

from constants import SQLITE_FILE
import sqlite3

class db:
    __connection__ = None
    
    def __init__(self):
        self.connection = sqlite3.connect(SQLITE_FILE)
        c = self.connection.cursor()

        # Create table
        c.execute('''
                create table if not exists composers(
                            generation integer,
                            parent integer,
                            gene text, 
                            status text)
                ''')

        self.commit()
        c.close()
       
    def __commit__(self):
        self.connection.commit()

    def __cursor__(self):
        return self.connection.cursor()

    #Commits all transactions which aren't committed and closes db connection
    def close(self): 
        self.connection.close()
        
    
    #Inserts new song and returns its id
    def put(self, generation, parent, genome, status):
        c = self.cursor()
        c.execute('''
                INSERT INTO composers  VALUES (?,?,?,?)
                ''', (generation,parent,gene,status))

        self.commit()
        c.execute('''
                SELECT ROWID FROM composers ORDER BY ROWID DESC LIMIT 1
                ''')
        rowid = c.fetchall()
        c.close()
        return rowid[0][0]
    
    #Returns composer for the given row id
    def get(self, rowid):
        c = self.cursor()
        c.execute('''
                SELECT * FROM composers WHERE ROWID=?
                ''',(rowid))
        result = c.fetchall()
        return result[0]
    
    #Updates status of the given row id
    def update(self, rowid, status):
        c = self.cursor()
        c.execute('''
                UPDATE composers SET status=? WHERE ROWID=?
                ''', (status, rowid))
        self.commit()
    
    #prints all table with column names  ROWID | GENERATION | PARENT | GENE | STATUS
    def printAll(self):
        c=self.cursor()
        c.execute('SELECT ROWID,generation,parent,gene,status FROM COMPOSERS ORDER BY ROWID DESC')
        for row in c:
            print(row)
