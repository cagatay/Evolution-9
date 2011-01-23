'''
Created on Oct 11, 2010

@author: melih.karci
'''

from constants import SQLITE_FILE
import sqlite3
import json

class db:
    _connection = None
    
    def __init__(self):
        self._connection = sqlite3.connect(SQLITE_FILE)
        c = self._connection.cursor()
        
        # Create neural networks table
        c.execute('''
            CREATE TABLE IF NOT EXISTS neural_networks(
                name TEXT PRIMARY KEY ON CONFLICT REPLACE,
                dataset TEXT,
                trained BOOLEAN
            );
        ''')

        # Create saved table
        c.execute('''
            CREATE TABLE IF NOT EXISTS evolutions(
                name TEXT PRIMARY KEY ON CONFLICT REPLACE,
                population_size INTEGER,
                generation_count INTEGER,
                evaluator TEXT,
                initialized BOOLEAN,
                FOREIGN KEY(evaluator) REFERENCES neural_networks(name)
            );
        ''')

        # create genomes table
        c.execute('''
            CREATE TABLE IF NOT EXISTS genomes(
                id INTEGER PRIMARY KEY ON CONFLICT REPLACE,
                genome TEXT,
                evolution TEXT,
                parent_1 INTEGER,
                parent_2 INTEGER,
                status TEXT,
                FOREIGN KEY(evolution) REFERENCES evolutions(name)
            );
        ''')

        self._commit()
        c.close()
       
    def _commit(self):
        self._connection.commit()

    @property
    def _cursor(self):
        return self._connection.cursor()

    def close(self): 
        self._connection.close()
    
    def save_evolution(self, name, population_size, evaluator, generation_count, initialized):
        c = self._cursor
       
        c.execute('''
            INSERT INTO evolutions (name, evaluator, population_size, generation_count, initialized)
                VALUES(?, ?, ?, ?, ?);
        ''', (name, evaluator, population_size, generation_count, int(initialized)))
        self._commit()

        c.close()
        return

    #Returns evolution for the given row id
    def get_evolution(self, name):
        c = self._cursor()
        c.execute('''
            SELECT * FROM evolutions WHERE name=?
        ''', (name))

        result = c.fetchall()
        c.close()

        return result[0] if result else None

    def get_evolution_list(self):
        c = self._cursor()
        c.execute('''
            SELECT name FROM evolutions
        ''')
        
        result = c.fetchall()
        c.close()

        return result
    
    def new_neural_network(self, name, dataset):
        c = self._cursor
       
        c.execute('''
            INSERT INTO neural_networks (name, dataset, trained)
                VALUES(?, ?, ?);
        ''', (name, json.dumps(dataset), 0))
        self._commit()

        c.close()
        return 

    def update_neural_network(self, row_id, trained):
        c = self._cursor

        c.execute('''
            UPDATE neural_networks SET trained=?  WHERE name=?;
        ''', (int(trained), row_id))

        self._commit()
        c.close()

        return

    def get_neural_network(self, name):
        c = self._cursor

        c.execute('''
            SELECT dataset, trained from neural_networks WHERE name=?;
        ''', [name])

        result = c.fetchall()[0]

        c.close()

        return json.loads(result[0]), bool(result[1])

    def get_neural_network_list(self):
        c = self._cursor
        c.execute('''
            SELECT name FROM neural_networks
        ''')
        
        result = c.fetchall()
        c.close()

        return [x[0] for x in result]

    #Updates status of the given row id
    def update(self, rowid, status):
        c = self.cursor()
        c.execute('''
            UPDATE composers SET status=? WHERE ROWID=?
        ''', (status, rowid))

        self.commit()

        c.close()
        return
