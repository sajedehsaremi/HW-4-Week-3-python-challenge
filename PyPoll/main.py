# Import dependencies
import os
import csv

from collections import Counter

## Set Path for files
csvpath = os.path.join("PyPoll\Resources", "election_data.csv")

# Summary Output files
output_file = os.path.join("python-challenge", "PyPoll", "Analysis_Summary.txt")

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv file
with open("C:/Users/Sajedeh/personal-class/gt-atl-data-pt-06-2021-u-c/03-Python/02-Homework/Instructions/PyPoll/Resources/election_data.csv", newline="", encoding="utf-8") as elections:

    # Creat the contents of budget_data.csv in the variable csvreader
    Elections = csv.reader(elections,delimiter=",")
    print(Elections)

# Creat list based on CSV columns
    file = csv.DictReader(elections)
    VoterID = []
    Candidate = []
    County = []

    for col in file:
        VoterID.append(col["Voter ID"])
        Candidate.append(col["Candidate"])
        County.append(col["County"])
    # print(VoterID)
    # print(County)
    # print(Candidate)


    print("Total number of votes:", len(VoterID))
# Creat the details of candidates and their accomplished 

    Candidate_count = Counter(Candidate)
    print("A complete list of candidates who received votes", Candidate_count.keys())
    for key, value in Candidate_count.items():
        print("The percentage of votes for candidate", key, "is", (100 * value)/len(Candidate), "%", "which  is equal to" , value, " number of votes.")

    Winner = max(Candidate_count, key=Candidate_count.get)
    print( "The winner of the election is " , Winner, "!")
