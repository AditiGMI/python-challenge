import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

#defining variable for results
Total_votes = 0
Candidate = []
List_candidate = []
Candidate_vote = {}
Winner = ""
Winner_count = 0

#reading the first line of the csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        #counting the total number of months 
        Total_votes += 1
        for row in csvreader:
             Total_votes += 1
             if row[2] not in Total_votes:
                 Total_votes[row[2]] = 1
             else : 
                 Total_votes[row[2]] += 1
        Candidate = row[2]
        if Candidate not in List_candidate:
            List_candidate.append(Candidate)
            Candidate_vote[Candidate] = 0
            Candidate_vote[Candidate] = Candidate_vote[Candidate]+1 


#printing the results
print("Election Results")
print("-------------------------")
print(f"Total votes: {Total_votes}")
print(f"Candidates: {Candidates}")
print(f"Average Change: {Average_change}")
print(f"Greatest increase: {Greatest_increase_in_Profits}")

# open the output file, then write 
f = open("pypoll_output.txt", "w")
f.write("Election Results")
f.write("-------------------------")
f.write(f"Total votes: {Total_votes}")
f.write(f"Total amount: {Total_profit_loss}")
f.write(f"Average Change: {Average_change}")
f.write(f"Greatest increase: {Greatest_increase_in_Profits}")
f.write(f"Greatest Decrease: {Greatest_decrease_in_Profits}")
