#!/usr/bin/env python3
# Welcome

import os
import sys
import mysql.connector



db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Ktim36210^*^",
	database = "myalias",
	auth_plugin = "mysql_native_password"
)
mycursor = db.cursor()
mycursor.execute("USE myalias")

welcome = "Welcome!"

os.system('ls')
os.system('./welcome-my-alias.sh')
print(welcome.center(620) + 
	"{0:>3}".format("1. List aliases").center(600) +
	"{0:>3}".format("2. View alias").center(600) + 
	"{0:>3}".format("3. Add alias").center(600) + 
	"{0:>3}".format("4. Modify alias").center(600) + 
	"{0:>3}".format("5. Remove alias").center(600) + 
	"{0:>3}".format("6. Exit").center(600) + 
	sys.version)
choice = input("Choose: ")



def listaliases():
   os.system("figlet -c -t -f standard 'LIST ALIASES' |lolcat")
   mycursor.execute("SELECT userID, username, systemname FROM Users INNER JOIN Systems ON Users.systemID = Systems.systemID")
   print("X------X--------------------X--------------------X")
   print("|  XX  |      Username      |       System       |")
   print("X------X--------------------X--------------------X")
   whitespaceUsername = ""
   whitespaceSystem = ""
   for user in mycursor:
      spacesUsername = 20 - int(len(user[1])) - 1
      spacesSystem = 20 - int(len(str(user[2]))) - 1
      for i in range(spacesUsername):
         whitespaceUsername += "‎‎‏‏‎ ‎"
      for i in range(spacesSystem):
         whitespaceSystem += "‎‎‏‏ ‎"
      print("|  0" + str(user[0]) + "  | " + user[1] + whitespaceUsername + "| " + str(user[2]) + whitespaceSystem + "|")
      whitespaceUsername = ""
      whitespaceSystem = ""
   print("X------X--------------------X--------------------X")


def viewalias():
   os.system("figlet -c -t -f standard 'VIEW ALIAS' |lolcat")

def createalias():
   os.system("figlet -c -t -f standard 'CREATE ALIAS' |lolcat")
   firstname = input("FIRST NAME: ")
   lastname = input("LAST NAME: ")
   username = input("USERNAME: ")
   systemname = input("SYSTEM: ")
   userID = 0
   systemID = 0
   mycursor.execute("SELECT * FROM Users")
   for user in mycursor:
      userID = user[2] + 1
   mycursor.execute("SELECT * FROM Systems")
   for system in mycursor:
      systemID = system[0] + 1
   mycursor.execute("INSERT INTO Systems(systemID, systemname) VALUES(%s, %s)", (systemID, systemname))
   mycursor.execute("INSERT INTO Users(userID, username, systemID) VALUES(%s, %s, %s)", (userID, username, systemID))
   db.commit()

def modifyalias():
   os.system("figlet -c -t -f standard 'MODIFY ALIAS' |lolcat")

def removealias():
   os.system("figlet -c -t -f standard 'REMOVE ALIAS' |lolcat")
   username = input("USERNAME: ")
   mycursor.execute("SELECT * FROM Users")
   for user in mycursor:
      if user[1] == username:
         print(user)
         print(user[1])
         mycursor.execute("DELETE FROM Users WHERE username = 'B'") 
         #db.commit()

def exit():
   os.system("")



if (choice == "1"):
   listaliases()
elif (choice == "2"):
   viewalias()
elif (choice == "3"):
   createalias()
elif (choice == "4"):
   modifyalias()
elif (choice == "5"):
   removealias()
else:
   exit()
