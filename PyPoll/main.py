import os
import csv

csvpath =os.path.join("..","PyPoll", "election_data.csv")

with open(csvpath, newline='') as candidateFile:
    csvreader = csv.reader(candidateFile, delimiter=',')
    csv_header = next(csvreader)

    totalVotes = 0
    candidates = []
    candidate1 = 0
    candidate2 = 0
    candidate3 = 0
    candidate4 = 0
    winner = ""

    for row in csvreader:
        totalVotes +=1

        #find unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])

        #count how many times they appear in the poll data as this is their total votes
        if candidates[0] == row[2]:
            candidate1 +=1
        elif candidates[1] == row[2]:
            candidate2 +=1
        elif candidates[2] == row[2]:
            candidate3 +=1
        elif candidates[3] == row[2]:
            candidate4 +=1

        #determine winner
        if (candidate1 > candidate2) and (candidate1 > candidate3) and (candidate1 > candidate4):
            winner = candidates[0]
        elif (candidate2 > candidate1) and (candidate2 > candidate3) and (candidate2 > candidate4):
            winner = candidates[1]
        elif (candidate3 > candidate1) and (candidate3 > candidate2) and (candidate3 > candidate4):
            winner = candidates[2]
        elif (candidate4 > candidate3) and (candidate4 > candidate2) and (candidate4 > candidate1):
            winner = candidates[3]

    #format variables
    candidate1Percent = "{:.3f}".format((candidate1/totalVotes)*100)
    candidate2Percent = "{:.3f}".format((candidate2/totalVotes)*100)
    candidate3Percent = "{:.3f}".format((candidate3/totalVotes)*100)
    candidate4Percent = "{:.3f}".format((candidate4/totalVotes)*100)

    #print to terminal
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {totalVotes}')
    print("-------------------------")
    print(f'{candidates[0]}: {candidate1Percent}% ({candidate1})')
    print(f'{candidates[1]}: {candidate2Percent}% ({candidate2})')
    print(f'{candidates[2]}: {candidate3Percent}% ({candidate3})')
    print(f'{candidates[3]}: {candidate4Percent}% ({candidate4})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")

#print to txt file
output_path = os.path.join("..", "PyPoll", "election_results.txt")
with open(output_path, 'w', newline='') as electionResultsFile:
    electionResultsFile.write("Election Results\n")
    electionResultsFile.write("-------------------------\n")
    electionResultsFile.write(f'Total Votes: {totalVotes}\n')
    electionResultsFile.write("-------------------------\n")
    electionResultsFile.write(f'{candidates[0]}: {candidate1Percent}% ({candidate1})\n')
    electionResultsFile.write(f'{candidates[1]}: {candidate2Percent}% ({candidate2})\n')
    electionResultsFile.write(f'{candidates[2]}: {candidate3Percent}% ({candidate3})\n')
    electionResultsFile.write(f'{candidates[3]}: {candidate4Percent}% ({candidate4})\n')
    electionResultsFile.write("-------------------------\n")
    electionResultsFile.write(f'Winner: {winner}\n')
    electionResultsFile.write("-------------------------")


        


