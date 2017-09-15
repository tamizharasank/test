import pandas as pd
import numpy
from pandas import ExcelWriter
from pandas import ExcelFile
import MySQLdb

def create_table():
	df = pd.read_excel('w.xls', sheetname='Sheet1')
	l=[]
	for x in  df.columns:
		l.append(x)
	
	
	con=MySQLdb.connect("localhost","root","tam","ifet")
   	obj=con.cursor() 
	table_name = "tt"
	createsqltable = "CREATE TABLE IF NOT EXISTS "  + table_name + " (" + " varchar(450),".join(l) + " varchar(450))"
	print createsqltable
	obj.execute(createsqltable)
	con.commit()
def insert_table():
	df = pd.read_excel('w.xls' , sheetname='Sheet1')
	l=[]
	ll=[]
	con=MySQLdb.connect("localhost","root","tam","ifet")
   	obj=con.cursor() 
	for x in  df.columns:
		l.append(x)
	
	values = df.values
	for x in values:
		ll.append(x)
		print x
	table_name = "tt"
   	e="'%s',"*len(l)
	e=e[0:len(e)-1]
	y=" VALUES("+e+")"
	for x in ll:
		q=tuple(x)
		ta="INSERT INTO "  + table_name + " (" + ", ".join(l) + ")" +y %(q)
		obj.execute(ta)
		con.commit()
if __name__=="__main__":
	create_table()
	insert_table()