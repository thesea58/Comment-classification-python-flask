import pyodbc 
from datetime import datetime
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
def connection_SQL_local():
    server = 'localhost' 
    database = 'comment' 
    username = 'sa' 
    password = 'lifelong' 
    #ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+'; UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cnxn,cursor
def connection_SQL():
    server = 'theseaserver.database.windows.net'
    database = 'comment'
    username = 'user_sql_server'
    password = '{*Phanloaicomment#}'   
    driver= '{ODBC Driver 17 for SQL Server}'

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cnxn,cursor

#Sample select query
def insert_DATA(comment,label):
    cnxn,cursor = connection_SQL()
    currentDateAndTime = datetime.now()

    smalldatetime = currentDateAndTime
    count = cursor.execute("""INSERT INTO dbo.comment_table(noi_dung,class,ngay_them) 
                    VALUES (?,?,?)""",comment,label,smalldatetime).rowcount
    cnxn.commit()
    print('Rows inserted: ' + str(count))

# VIEW TABLE
# cursor.execute("SELECT * FROM comment_table;")
# row = cursor.fetchone() 
# while row: 
#     print(row)
#     row = cursor.fetchone()


