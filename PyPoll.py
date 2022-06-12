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


     # Open the election results and rad the file.
     with open (file_to_load) as election_data:

          # To do: read and analyze the data here.
          # Read the file obect with the reader function.
          file_reader = csv.reader(election_data)

          # Print each row in the CSV file.
          # for row in file_reader:
               #print(row)

          # Readthe file object with the reader function
          file_reader = csv.reader(election_data)

          # Print the header row.
          headers = next(file_reader)
          print(headers)

