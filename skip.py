import os

while True: 
	print "Skip?"
	skip = raw_input()
	if skip == "s":
		os.system("sudo pkill pi_fm_rds")
		os.chdir("../../")
		os.system("ls")
		os.system("./station.sh")
	if skip == "stop":
		os.system("sudo pkill pi_fm_rds")
		os.system("sudo pkill python")
