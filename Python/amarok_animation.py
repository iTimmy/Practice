#!/usr/bin/env python3
	
import os, time

os.system('')
username = input("Username: ")

COLORS = {\
	"black":"\u001b[30;1m",
	"red":"\u001b[31;1m",
	"green":"\u001b[32m",
	"yellow":"\u001b[33;1m",
	"blue":"\u001b[34;1m",
	"magenta":"\u001b[35m",
	"cyan": "\u001b[36m",
	"white":"\u001b[37m",
	"yellow-background":"\u001b[43m",
	"black-background":"\u001b[40m",
	"cyan-background":"\u001b[46;1m",
	"RESET":"\u001b[0m",
}

def colorText(text):
	for color in COLORS:
		text = text.replace("[[" + color + "]]", COLORS[color])
	return text

def correct():
	loadbar = "[[cyan-background]][[white]]"
	for i in range(70):
		print(colorText(loadbar))
		print(colorText("[[RESET]]Loading in progress..."))
		loadbar += "=="
		time.sleep(0.1)
		os.system('clear')

if username == "iTimmy":
        correct()
else:
        print(colorText("Incorrect."))
