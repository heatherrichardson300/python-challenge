import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "blank_test.txt")  # Output file path

#colums to list
ballot_id = []
county = []
candidate = []

candidate_names = set()

total_votes = 0 
candidate_count = {}


with open(file_to_load, 'r') as election_data:
    csvreader = csv.reader(election_data)
    header = next(csvreader)
    
    for row in csvreader:

        total_votes += 1
        name = row[2]
        
        if name in candidate_count:
            candidate_count[name] += 1
        else:
            candidate_count[name] = 1

        candidate_names.add(row[2])

    def election_totals():

        for name, count in candidate_count.items():
            percentage_votes = ( count / total_votes ) * 100
            print(f"{name}: {count} votes, {percentage_votes:.3f}%")
            
            winner_name = max(candidate_count, key=candidate_count.get)
            
            print(f"Winner: {winner_name}")

        print("Total Votes: " + str(total_votes))
    election_totals()

# with open(file_to_output, 'w') as newcsvfile:
#     newcsvfile.write("Election Summary and Results\n")
#     newcsvfile.write(str(election_data))
