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
vote_pcts = {}
for candidate in candidate_list:
	vote_pcts[candidate] = (votes[candidate]/total_votes)*100


#  Winner is determined as candidate with highest percentage of votes:
winner = max(vote_pcts, key=vote_pcts.get)

#  A complete list of candidates who received votes, with applicable % and vote counts
#  Output is saved to external file

analysis_file = os.path.join('analysis', 'analysis_file.txt')
with open(analysis_file, "w", newline = "") as outfile:
    print("Election Results",file = outfile)
    print("----------------------------", file = outfile)
    print(f'Total Votes: {total_votes}', file = outfile)
    print("----------------------------", file = outfile)
    for candidate in candidate_list:
        print (f'{candidate}: {vote_pcts[candidate]: .3f}% ({votes[candidate]})', file = outfile)
    print("----------------------------", file = outfile)
    print(f'Winner: {winner}', file = outfile)
    print("----------------------------", file = outfile)


with open(analysis_file, "r", newline = "") as outfile:

	print(outfile.read())
