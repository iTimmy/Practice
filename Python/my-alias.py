#!/usr/bin/env python
# Welcome

import os



welcome = "Welcome!"
options = "1. List aliases\n2. View alias" 	

os.system('ls')
os.system('./welcome-my-alias.sh')
print(welcome.center(620) + 
	"{0:>3}".format("1. List aliases").center(600) +
	"{0:>3}".format("2. View alias").center(600) + 
	"{0:>3}".format("3. Modify alias").center(600) + 
	"{0:>3}".format("4. Modify alias").center(600) + 
	"{0:>3}".format("5. Remove alias").center(600) + 
	"{0:>3}".format("6. Exit").center(600))
choice = input("Choose: ")



def listaliases():
	os.system("figlet -c -t -f standard 'LIST ALIASES' |lolcat")

def viewalias():
	os.system("figlet -c -t -f standard 'VIEW ALIAS' |lolcat")
	os.system("echo '                                      '")
	os.system("echo '                                      '")
	os.system("echo '                                      '")
	os.system("echo '                                      '")
	os.system("echo '                                      '")
	os.system("echo '                                      '")


def createalias():
	os.system("figlet -c -t -f standard 'CREATE ALIAS' |lolcat")
	os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")


def modifyalias():
	os.system("figlet -c -t -f standard 'MODIFY ALIAS' |lolcat")
	os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")


def removealias():
	os.system("figlet -c -t -f standard 'REMOVE ALIAS' |lolcat")
	os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")
        os.system("echo '                                      '")


def exit():
	os.system("")



if (choice == 0):
    	listaliases()
elif (choice == 1):
	viewalias()
elif (choice == 2):
	createalias()
elif (choice == 3):
	modifyalias()
elif (choice == 4):
	removealias()
else:
	exit()
