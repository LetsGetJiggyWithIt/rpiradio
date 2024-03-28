





#---------------------------------------------------------------------------------------#
#----------------------PiFmRds Radio Station Code v1 By Vaughn Palmer-------------------#
#---------------------------------------------------------------------------------------#


This code was written to create a more effective way to play .wav files using PiFmRds
through the shell. Recently found out this may be a less-functional version of
morrolinux's mpradio here: https://github.com/morrolinux/mpradio
I still had a great time building this, and learned a lot from the experience.

This is not under active development, but I may come back to this from time to time.

#-------------------------------------Neccessary files----------------------------------#


# PiFmRds Package - Prefferably in home/pi

# station.py - Creates the radio station

# Sound files - You know, for broadcasting?




#------------------------------Optional (And suggested) files---------------------------#


# stop.sh - Used for stopping both the python proccess and the bash command

# mount.sh - Will auto mount your media for external storage (Running at startup suggested)

# skip.py - Runs along with the "station.sh" file. Allows user to type "s" to skip current song

# station.sh (In home/pi) - Adds convenience for running on system start as well as adding skip feature

# radio.py - Allows for the playing of individual songs with ease

# radio.sh (In home/pi) - Adds the convenience for running on start as well as from the default directory

# songlist.txt - Allows for easier use of radio.py

# restart.sh (In home/pi) and restart.py - Restarts the Radio Station

# s.sh - Used by skip.py

# unmount.sh - Allows for easier hardware ejection through command line




#-----------------------------------------How To Use------------------------------------#





I coded this using a Raspberry Pi running Raspbian lite (Minimal version) through the command line. I have
not tested this on a graphical interface, so feel free to test it however you wish.

This entire code is based off the assumption that you have PIFmRds installed in your home directory on your
Raspberry Pi. If this is not the case, either reinstall the package to your home directory or change the
code to your preference.

To use the code, run station.sh and allow it to run. This should auto play all the .wav files put in
your chosen directory. (This can be changed by editing "station.py") These will be broadcast to 94.3
FM. If you chose to use "skip.py", you should also be getting a prompt from the command line to skip
the current song. To do this, type "s" and hit enter. It should skip to another random song. All
songs should be numbered. (e.g; 1.wav, 2.wav) Edit the songlist according to the songs in your folder.

Immediately after running radio.sh you should get a prompt asking which frequency you should broadcast to.
When left blank it will default to 94.3. After being prompted for the frequency you will be asked which
file to play. This program will automatically look in home/pi/Music/PiFmRds unless changed in
station.py

Running restart.sh will kill all current python proccesses and will afterwards run station.py In turn,
stop.sh will do the same thing but it will not start another proccess.

The file mount.sh and unmount.sh were created so I wouldn't have to manually mount/unmount my USB every
time I wanted to remove it from my pi.

If you have any questions or concerns about this project, feel free to contact me at vpalmscholar@gmail.com
