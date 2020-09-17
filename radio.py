#Imports the "os" Python library for shell commands

import os

#Defines the "list" function
list1 = open("songlist.txt")
list = list1.read()

#Prompts User for Broadcast Frequency and sets it to a variable for later use
print("What frequency would you like to broadcast to? (Default is 94.3)")
freq = raw_input()

#Sets frequency to 94.3 if left blank
if freq == "":
	freq = "94.3"

#Prompts user for song file name and saves to a variable for later use
print('What song would you like to play? (Type "list" for song list)')
audio1 = raw_input()
while audio1 == "list":
	print list
	print 'What song would you like to play? (Type "list" for song list'
	audio1 = raw_input()
audio = "Music/PiFmRds" + audio1

#Compiles Variables Into a Shell Command
radio = "sudo ./pi_fm_rds -freq " + freq + " -audio " + audio + ".wav &"

#Kills Previous  radio.py Command
os.system("sudo pkill pi_fm_rds")

#Runs New Radio Command
os.system(radio)
print "Broadcasting to " + freq + " FM..."
