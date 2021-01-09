#PyPoll

import os
import csv

# Dataset: [election_data.csv](PyPoll/Resources/election_data.csv). 

election_data = os.path.join("Resources", "election_data.csv")

# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

candidate_list = []

with open(election_data) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')
		
	#Read the header row first
	csv_header = next(csvreader)
	total_votes = 0

	import collections
	votes = collections.Counter()

#Python script analyzes the votes and calculates each of the following:
	
#  The total number of votes cast
#	Count # of rows (skipping first line)
	for row in csvreader:
		total_votes +=1
		votes[row[2]]+=1

		candidate_name = (row[2])

		if candidate_name not in candidate_list:
			candidate_list.append(candidate_name)
		

#  The percentage of votes each candidate won, formatted as a percentage:
vote_pct_1 = ((votes[candidate_list[0]]/total_votes)*100)
vote_pct_2 = ((votes[candidate_list[1]]/total_votes)*100)
vote_pct_3 = ((votes[candidate_list[2]]/total_votes)*100)
vote_pct_4 = ((votes[candidate_list[3]]/total_votes)*100)

vote_pcts = {candidate_list[0]: int(vote_pct_1),
	candidate_list[1]: int(vote_pct_2),
	candidate_list[2]: int(vote_pct_3),
	candidate_list[3]: int(vote_pct_4)
	}

#  Winner is determined as candidate with highest percentage of votes:
winner = max(vote_pcts, key=vote_pcts.get)

#  A complete list of candidates who received votes, with applicable % and vote counts
#  Output is saved to external file

analysis_file = os.path.join('analysis', 'analysis_file.txt')
with open (analysis_file, "w", newline = "") as outfile:
	print ("Election Results",file = outfile)
	print ("----------------------------", file = outfile)
	print (f'Total Votes: {total_votes}', file = outfile)
	print ("----------------------------", file = outfile)
	print (f'{candidate_list[0]}: {vote_pct_1: .3f}% ({votes[candidate_list[0]]})', file = outfile)
	print (f'{candidate_list[1]}: {vote_pct_2: .3f}% ({votes[candidate_list[1]]})', file = outfile)
	print (f'{candidate_list[2]}: {vote_pct_3: .3f}% ({votes[candidate_list[2]]})', file = outfile)
	print (f'{candidate_list[3]}: {vote_pct_4: .3f}% ({votes[candidate_list[3]]})', file = outfile)
	print ("----------------------------", file = outfile)
	print (f'Winner: {winner}', file = outfile)
	print ("----------------------------", file = outfile)


with open(analysis_file, "r", newline = "") as outfile:

	print(outfile.read())
