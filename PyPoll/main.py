# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import csv

row_count = 0
total_profit = 0
pl_current_month = 0
pl_previous = 0
# next_month = ""
change_mtm_sum = []
# profit_losses = []
test = []
# save the output file path
election_data = r"C:\Users\vb_ab\pythonfiles\homework\python_challenge\election_data.csv"

dates_for_change = {}
candidate_list = []

with open(election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    candidate_list1 = []
    candidates = []
    newdict = {}
    khan_count = 0
    for row in csvreader:
        # Store data from row into lists
        voter_ids = row[0]
        counties = row[1]
        candidates = row[2]
        row_count += 1
        candidate_list.append(candidates)
        newdict[voter_ids] = candidates

print(candidate_list.count("Khan"))
print(candidates.count("Khan"))
print(newdict)

#print(candidate_list)
no_repeat = set(candidate_list)
print(no_repeat)
total_votes = row_count

khan_votes = candidate_list.count("Khan")
khan_percent = khan_votes / total_votes
print(khan_percent * 100)
correy_votes = candidate_list.count("Correy")
correy_percent = correy_votes / total_votes
print(correy_percent * 100)
otooley_votes = candidate_list.count("O'Tooley")
otooley_percent = otooley_votes / total_votes
print(otooley_percent * 100)
li_votes = candidate_list.count("Li")
li_percent = li_votes / total_votes

print("Khan total: " + str(khan_votes))
print(f"{khan_percent:.3%}")

print("Correy total: " + str(correy_votes))
print(f"{correy_percent:.3%}")

print("O'Tooley total: " + str(otooley_votes))
print(f"{otooley_percent:.3%}")

print("Li total: " + str(li_votes))
print(f"{li_percent:.3%}")

print("Election Results")

#print(khan_count)
print("-------------------------")
print("Total Votes:" +  " " + str(total_votes))
print("-------------------------")
