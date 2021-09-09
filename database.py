import pymysql
from model import Grocery
con = pymysql.connect(host='localhost',user='root',passwd='',db='grocerydb')
print('Connected Successfully with Database...')
cursor = con.cursor()

def saveGroc(groc):
    try:
        sqlQuery = 'insert into grocery (grocName,grocPrice,grocImg,grocType,grocQuantity) values (%s,%s,%s,%s,%s)'
        cursor.execute(sqlQuery,(groc.grocName,groc.grocPrice,groc.grocImg,groc.grocType,groc.grocQuantity))
        con.commit()
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)

def getGroclist():
    groclist =[]
    try:
        sqlQuery = 'select * from grocery'
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        con.commit()
        for row in rows:
            # Create the object of table Grocery
            groc = Grocery(row[0],row[1],row[2],row[3],row[4],row[5])
            groclist.append(groc)
        else:
            return groclist
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)

def deleteGroc(_id):
    try:
        sqlQuery = 'delete from grocery where grocId = %s'
        cursor.execute(sqlQuery,(_id))
        con.commit
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)

def updateGroc(_id,groc):
    try:
        sqlQuery= 'update grocery set grocName=%s,grocPrice=%s,grocImg=%s,grocType=%s,grocQuantity=%s where grocId=%s'
        cursor.execute(sqlQuery,(groc.grocName,groc.grocPrice,groc.grocImg,groc.grocType,groc.grocQuantity,_id))
        con.commit() 
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)

def getGrocById(_id):
    try:
        sqlQuery ='select * from grocery where grocId = %s'
        cursor.execute(sqlQuery,(_id))
        row = cursor.fetchone()
        groc = Grocery(row[0],row[1],row[2],row[3],row[4],row[5])
        con.commit()
        return groc
    except Exception as e:
        print("-"*5,'Error',"-"*5)
        print(e)

def closeconnection():
    con.close()
        
        