# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_names = set()
candidate = []
election_data = []

# Winning Candidate and Winning Count Tracker
total_votes = 0 
candidate_count = {}

# Open the CSV file and process it
with open(file_to_load, encoding="UTF-8") as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate in candidate_count:
            candidate_count[candidate] += 1
        else:
            candidate_count[candidate] = 1

        candidate_names.add(row[2])

        # Add a vote to the candidate's count
        
winner_name = max(candidate_count, key=candidate_count.get)
# Open a text file to save the output

with open (file_to_output, 'w') as txt_file:

    # Write the total vote count to the text file
    txt_file.write("ELECTION SUMMARY AND RESULTS\n")
    txt_file.write("____________________________\n")

    election_data = [
        f'\nTotal Votes: {total_votes}',
        "____________________________"
    ]
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, count in candidate_count.items():

        # Get the vote count and calculate the percentage
        percentage_votes = (count / total_votes) * 100

        # Update the winning candidate if this one has more votes
        # Print and save each candidate's vote count and percentage
        election_data.append(f'\n{candidate}: {count} votes, ({percentage_votes:.3f}%)')
   
    # Generate and print the winning candidate summary
    
    election_data.append("____________________________")
    election_data.append(f'\nWinner: {winner_name}')
    election_data.append("____________________________")

    #print to terminal
    for line in election_data:
        print(line)
    
    #write to text file
    txt_file.write("\n".join(election_data))

