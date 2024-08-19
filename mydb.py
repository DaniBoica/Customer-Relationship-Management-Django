import mysql.connector

dataBase = mysql.connector.connect(

	host = 'localhost',
	user = 'root',
	passwd = 'admin1234'

	)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create database

cursorObject.execute("CREATE DATABASE danidb")

print( "All good ")