'''
Created on Oct 11, 2010

@author: melih.karci
'''

from constants import SQLITE_FILE
import sqlite3

class Database:
    __connection__ = None
    
    def initDatabase(self):
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
        c.close()
       
    #Commits all transactions which aren't committed and closes db connection
    def closeDatabase(self): 
        self.connection.commit()
        self.connection.close()
        
    
    #Inserts new composer and returns its id
    def newComposer(self,generation,parent,gene,status):
        c=self.connection.cursor()
        t =(generation,parent,gene,status)
        c.execute('''
                INSERT INTO composers  VALUES (?,?,?,?)
                ''',t)
        self.connection.commit()
        c.execute('''
                SELECT ROWID FROM composers ORDER BY ROWID DESC LIMIT 1
                ''')
        insertedRowId = c.fetchall()
        c.close()
        return insertedRowId[0][0]
    
    
    #Returns composer for the given row id
    def getComposer(self,rowId):
        t = (rowId,)
        c=self.connection.cursor()
        c.execute('''
                SELECT * FROM composers WHERE ROWID=?
                ''',t)
        result=c.fetchall()
        return result[0]
    
    #Updates status of the given row id
    def updateStatus(self,rowId,newStatus):
        t = (newStatus,rowId,)
        c=self.connection.cursor()
        c.execute('''
                UPDATE composers SET status=? WHERE ROWID=?
                ''',t)
        self.connection.commit()
    
    #prints all table with column names  ROWID | GENERATION | PARENT | GENE | STATUS
    def printAll(self):
        c=self.connection.cursor()
        c.execute('SELECT ROWID,generation,parent,gene,status FROM COMPOSERS ORDER BY ROWID DESC')
        for row in c:
            print(row)

        
        
        
       
        
        
    
    
        
        

