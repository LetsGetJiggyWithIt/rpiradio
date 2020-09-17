#----------------------------------------------------------------------------------------#
#-------------------------Assets (Do not edit unless fixing bugs!)-----------------------#
#----------------------------------------------------------------------------------------#








#-----------------------------------------Libraries-------------------------------------#


# Allows for the use of bash commands while in python
import os

# Imported this for a process I wanted to kill. (Still don't remember which one)
import subprocess

# Used to determine how long a song will play
import time

# Randomizes which song will come next
import random




#------------------------------------------Arrays---------------------------------------#


# Array of song names (All are named after numbers for convenience)
songs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46"]

# Array of song durations (Only way I've found so far to get them to stop on their own)
duration = [21, 103, 74, 197, 131, 31, 174, 233, 192, 177, 216, 223, 127, 207, 214, 220, 65, 81, 61, 631, 232, 60, 44, 142, 100, 217, 54, 224, 211, 232, 159, 168, 127, 192, 110, 110, 162, 111, 241, 80, 79, 560, 133, 273, 32, 133]




#-----------------------------------------Variables-------------------------------------#


# Defines which duration will be used in the "sleepy" variable
number = random.randint(0, 45)

# Defines how long the song will play (Based on how "number" is defined)
sleepy = duration [number]

# Define which song will play in relation to the duration
song = songs[number]




#--------------------------------------------Code---------------------------------------#


# For debugging. Gonna leave it in just in case
print song

# Defines the perameters needed for the bash command. (To change location of .wav files, just change the path name here)
command1 = "sudo ./pi_fm_rds -freq 94.3 -audio Music/PiFmRds"

# Adds the .wav file extension to the end and tells it to run in the background
command2 = ".wav &"

# Shows Users where they can tune in
print "Broadcasting on 94.3 FM..."

# Kills the previous proccess so they don't continue to pile up
os.system("sudo pkill pi_fm_rds")

# Running Loop
while True:

	# Redefines both song and duration variables
	sleepy = duration[number]
	song = songs[number]

	# Printing variables on screen (For debugging Purposes)
	print song
	print sleepy

	# Defines ccommand used by "os" library based on previously defined variables
	station = command1 + song + command2

	# Honestly, I don't remember why there's a blank command here. Feel free to experiment
	os.system("")

	# Runs the command defined two lines ago
	os.system(station)

	# Wait for the song duration
	time.sleep(sleepy)

	# Kills the last PiFmRds proccess
	os.system("sudo pkill pi_fm_rds")

	# Redefines the song and duration
	number = random.randint(0, 45)
	sleepy = duration[number]
	song = songs[number]

	# Debugging purposes.
	print song
	print sleepy
