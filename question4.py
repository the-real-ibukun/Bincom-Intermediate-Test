import psycopg2
import json

with open('groups.json') as f:
    data = json.load(f)


def create_tables1():
    """ ' create tables in the PostgreSQL database' """
    conn = None
    try:
        # read the connection parameters
        
        # connect to the PostgreSQL server
        conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        
        cur = conn.cursor()
        
        cur.execute('''CREATE TABLE groups
      (ID SERIAL PRIMARY KEY     NOT NULL ,
      G_NAME           TEXT    NOT NULL,
      MEMBERS      INT     NOT NULL
      );''')
        print ("Table created successfully")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            

def insert_groups():
    conn = None
    id = None
    try:
        conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()

        # """ INSERTING INTO DATABASE """    
        for i in data:
            cur.execute("INSERT INTO COL (G_NAME, MEMBERS) VALUES (%s,%s)   ",( i['Group Name'], i['Members']))
        # commit the changes
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

with open('post.json') as f:
    data2 = json.load(f)


def create_tables2():
    """ ' create tables in the PostgreSQL database' """
    conn = None
    try:
        # read the connection parameters
        
        # connect to the PostgreSQL server
        conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        
        cur = conn.cursor()
        
        cur.execute('''CREATE TABLE post
      (ID SERIAL PRIMARY KEY     NOT NULL ,
      NAMES           TEXT    NOT NULL,
      POST      INT     NOT NULL
      );''')
        print ("Table created successfully")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            

def insert_post():
    conn = None
    id = None
    try:
        conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()

        # """ INSERTING INTO DATABASE """    
        for i in data:
            cur.execute("INSERT INTO COL (NAMES, POST) VALUES (%s,%s)",( i['Name'], i['Post']))
        # commit the changes
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    