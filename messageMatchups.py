import csv
import subprocess

def main():
	roundNum = input("Enter round number: ")
	endDay = input("Enter day: ")

	# Get contacts from csv
	with open('contacts.csv', mode='r') as infile:
	    reader = csv.reader(infile)
	    contacts = {rows[0]:rows[1] for rows in reader}

	# Get matchups from csv
	with open('matchups.csv', mode='r') as infile:
		reader = csv.reader(infile)
		matchups = []
		for rows in reader: 
			matchups.append([rows[0],rows[1],rows[2]])

	for matchup in matchups: 
		print(matchup)
		p1Name = matchup[0]
		p2Name = matchup[1]
		endTime = matchup[2]

		p1Number = contacts.get(p1Name)
		p2Number = contacts.get(p2Name)
		print(p1Number)
		print(p2Number)

		message = constructMessage(p1Name, p2Name, roundNum, endDay, endTime)

		sendMessage(p1Number, p2Number, message)


def sendMessage(num1, num2, message): 
	scpt = '/Users/mumai/Desktop/BasketballTournament/sendMessage.applescript'

	args = [num1, num2, message]

	p = subprocess.Popen(
	        ['/usr/bin/osascript', scpt] + [str(arg) for arg in args], 
	        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	out, err = p.communicate()

	if p.returncode:
		print("Error", err)
	else: 
		print("Successfully sent messages!", out)


def constructMessage(p1Name, p2Name, roundNum, endDate, endTime):
	return ("Hey " + p1Name + " and " + p2Name + 
		   ", its Umair from the 2k tournament. Just wanted to remind you guys to play your " + roundNum +
		   " game before " + endDate + " at " + endTime + "PM" + 
		   ". What time would work for the both of you? Please checkout our updated rule set/format on the discord server." + 
		   " If you were planning on streaming (optional), send me the link and time so we can fit you in the schedule." + 
		   " Also please make sure to take a picture of the team comparison screen and post it on discord/send it here" + 
		   " (examples of what it would look like can be found in #scores on the discord). Thanks")

main()