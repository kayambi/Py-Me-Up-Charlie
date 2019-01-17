import os 
import csv 

candidates = []
total_votes = 0
counting_votes = []

csv_path = os.path.join('.','election_data.csv')

with open(csv_path, newline='') as csvfile:
    
     # csvreader specifies delimiter and variables that holds contents
        
    csvreader = csv.reader(csvfile, delimiter=',')
    line = next(csvfile)
    
    for line in csvreader: 
        
    # add total number of votes 
    
        total_votes = total_votes + 1 
    print(f" Total Votes:{total_votes}")
        
    #candidate voted for 
    
    candidate = line [2]
    
     #if candidate had another votes then add to vote tally
    
    if candidate in candidates : 
        candidate_index = candidates.index(candidate)
        counting_votes[candidate_index] = counting_votes[candidate_index] + 1 
        # else create a new spot in list for candidate
    else:
        #candidates.append()

        counting_votes.append(1)
        percentage = []
        max_votes = counting_votes [0]
        max_index = 0 
    print(f"{candidate[counting_votes ]}:{percentage[counting_votes ]}%({counting_votes[counting_votes ]}")

   
# find the percentage of vote for each candidate and winner

for count in range(len(candidates)):
    vote_percentage = counting_votes[count]/ total_votes * 100  
    percentage.append(vote_percentage)
    if counting_votes[count] > max(count):
        max_votes = counting_votes[count]
        print(max_votes)
    max_index = count 
    winner = candidate [max_index]

    
    #print(results)
    print("election results")
    print("-----------------")
    print(f" Total Votes:{total_votes}")
    
    for count in range(len(candidates)):
        print(f"{candidate[count]}:{percentage[count]}%({counting_votes[count]}")
        print("------------------------------------------------------")
        print(f"winner:{winner}")

    