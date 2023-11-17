import csv

# Define the path to the CSV file
file_path = "Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = []
votes_per_candidate = {}

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    next(csvreader, None)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Extract candidate name
        candidate = row[2]

        # Add candidate to the list if not already present
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 0

        # Count votes for each candidate
        votes_per_candidate[candidate] += 1

# Calculate the percentage of votes each candidate won
percentage_per_candidate = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

# Find the winner based on popular vote
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    print(f"{candidate}: {percentage_per_candidate[candidate]:.3f}% ({votes_per_candidate[candidate]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")