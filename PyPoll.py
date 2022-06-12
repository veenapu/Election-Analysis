#1. The data we need to retrieve.
#2, A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popluar vote.

import csv

import os

# Assign a variable for the file to load and the path.
# file_to_load = 'C:/Users/sonik/Documents/Bootcamp/UNC-VIRT-DATA-PT-05-2022-U-B/Election-Analysi/Resources/election_results.csv'
file_to_load = os.path.join('Resources', 'election_results.csv')


# Open the election results and read the file.
election_data = open(file_to_load, 'r')
# with open(file_to_load) as election_data:

# # To do: perform analysis.

# # # Close the file
election_data.close()

# # # Open the election results and read the file.
with open(file_to_load) as election_data:

#     #To do: perform analysis.
     print(election_data)



# # Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Traceback (most recent call last):
#   File "PyPoll.py", line 24, in <module>
#     open(file_to_save, "w")

#IOError: [Errno 2] No such file or directory: 'analysis/election_analysis.txt'

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # write some data to the file
     #txt_file.write("Hello World")

     # Write three counties to the file.
     # txt_file.write("Arapahoe, ")
     # txt_file.write("Denver, ")
     # txt_file.write("Jefferson")

     # or 2nd method to write the same
     #txt_file.write("Arapahoe, Denver, Jefferson")

     # To wrtie them in separate lines
     txt_file.write("Counties in the Election\n-------------------------\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")

     #Add our dependencies.
import csv
     
import os
     
     # Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources", "election_results.csv")

     # Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

     # 1. Initialize a total vote counter.
total_votes = 0

     # Candidate Options
candidate_options = []

     # 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and rad the file.
with open(file_to_load) as election_data:
     # Read the file obect with the reader function.
     file_reader = csv.reader(election_data)

          # Print each row in the CSV file.
          # for row in file_reader:
               #print(row)

          # Read the file object with the reader function
          # file_reader = csv.reader(election_data)

          # Read the header row.
     headers = next(file_reader)
          # print(headers)

          # Print each row in the CSV file.
     for row in file_reader:
          # 2. Add to the total vote count.
          total_votes += 1

# 3. Print the total votes.
# print(total_votes)

               # Print the candidate name from each row.
          candidate_name = row[2]

          if candidate_name not in candidate_options:
               # Add the candidate name to the candidate list.
               candidate_options.append(candidate_name)

               # 2. Begin tracking that candidate's vote count.
               candidate_votes[candidate_name] = 0

          # Add a vote to that candidate's count.
          candidate_votes[candidate_name] += 1

     # Save the results to our text file.
     with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
          election_results = (
          f"\nElection Results\n"
          f"--------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"--------------------------\n")
          print(election_results,end="")
# Save the final vote count to the text file.
          txt_file.write(election_results)

# Print the candidate vote dictionary.
print(candidate_votes)

# # Determine the percentage of votes for each candidate by looping through the counts.
# # 1. Iterate through the candidate_list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
     votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
     vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
     print(f"{candidate_name}: received {vote_percentage}% of the vote.")

# To do: print out the winning candidate, vote count and percentage to
# votes to the terminal.    
     # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


# Determine winning vote count and candidate
# 1. Determine if the votes is greater than the winning count.
     if (votes > winning_count) and (vote_percentage > winning_percentage):
          # 2. If true then set winning_count = votes and winning_percent =
          # vote_percentage. 
          winning_count = votes
          winning_percentage = vote_percentage
          # 3. Set the winning_candidate equal to the candidate's name.
          winning_candidate = candidate_name

# # To do: print out the winning candidate, vote count and percentage to
# # votes to the terminal.    
# print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# print(winning_candidate_summary)
winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")








