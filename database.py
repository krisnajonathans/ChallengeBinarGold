import sqlite3

def createTable():
    conn = sqlite3.connect("challenge.db")
    conn.execute("CREATE TABLE text (text varchar (255), clean_text varchar (255));")
    conn.execute("CREATE TABLE file (text varchar (255), clean_text varchar (255));")
    print("create table success")
    #commit the changes to db			
    conn.commit()
    #close the connection
    conn.close()    

def checkTable_text():
    conn = sqlite3.connect("challenge.db")
    c = conn.cursor()
                
    #get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='text' ''')

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : 
        print('Table text exists.')
    else : 
        return 0

def checkTable_file():
    conn = sqlite3.connect("challenge.db")
    c = conn.cursor()
                
    #get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='file' ''')

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : 
        print('Table file exists.')
    else : 
        return 0

def _insertText(a, b):
    conn = sqlite3.connect("challenge.db")
    conn.execute("insert into text (text, clean_text) values (?, ?)",(a, b))
    conn.commit()
    conn.close()
    print("Data berhasil disimpan di Database SQLite")

def _insertFile(a):
    a.rename(columns={'Tweet': 'text', 'space': 'clean_text'}, inplace=True)
    conn = sqlite3.connect('challenge.db') 
    a.to_sql('file', con=conn, index=False, if_exists='append') ## if_exists => replace => bikin tabel baru, menghapus yg lama
    conn.close()
    print("Data berhasil disimpan di Database SQLite")