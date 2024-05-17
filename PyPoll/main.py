import os 
import csv

# Create a path for the file in reference
PyPoll_File = os.path.join('.', 'Resources', 'election_data.csv')

# Open the CSV fle
with open(PyPoll_File, newline = '') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_reader)
    
    # Need to include the header in this case
    candidate_list = [candidate[2] for candidate in csv_reader]

# Calculate the total number of votes cast
total_votes = len(candidate_list)

# There are only 3 candidates and we are going to count out there individual total votes
candidates_votes = [[candidate, candidate_list.count(candidate)] for candidate in set(candidate_list)]
candidates_votes = sorted(candidates_votes, key = lambda x: x[1], reverse = True)

# Calculate the percentage of votes each candidate won
# Calculate the percent of votes using the percentage format
for candidate in candidates_votes:
    percentage_votes = (candidate[1] / float(total_votes)) * 100

# Print the results of votes as shown in the image
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")

for candidate in candidates_votes:
    percentage_votes = (candidate[1] / float(total_votes)) * 100
    # This print needs to be in a for loop, otherwise it will only print the last candidate
    # Print the percentages in 6.3 format (6 since there will be 6 digits in total, includign the decimal, and 3 for three spaces after the decimal)
    print(f'{candidate[0]}: {percentage_votes: 6.3f}% ({candidate[1]})')

print("----------------------------------")
print(f"Winner: {candidates_votes[0][0]}")
print("----------------------------------") 


# Print the results of the code to a text file
# Need to make a new path to create a new text file
PyPoll_Results = os.path.join('.', 'Analysis', 'PyPoll_Results_Text.txt')
with open(PyPoll_Results, "w") as text_file:
    print("Election Results", file = text_file)
    print("------------------------------------", file = text_file)
    print(f"Total Votes: {total_votes}", file = text_file)
    print("------------------------------------", file = text_file)

    # need to make a for loop in order to print all three candidates names
    for candidate in candidates_votes:
        # need to reuse percentage_votes calculation since it will just write the first candidate's percentage in the text
        percentage_votes = (candidate[1] / float(total_votes)) * 100
        print(f'{candidate[0]}: {percentage_votes: 6.3f}% ({candidate[1]})', file = text_file)

    print("------------------------------------", file = text_file)
    print(f"Winner: {candidates_votes[0][0]}", file = text_file)
    print("------------------------------------", file = text_file)

