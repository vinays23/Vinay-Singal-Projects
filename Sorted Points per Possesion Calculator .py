# Objective: Create a viable points per possession calculator for a basketball team of 12 players, and rank the players based on their ppp value.

# STEP 1: Initialize a dictionary.

pos_efficiency = {}

#STEP 2: Create a loop which runs 12 times.

for i in range(1, 13):
    while True:
        
        #STEP 3: Force the user to make the correct inputs.
        
        try:
            jersey_num = int(input("Enter player {}'s jersey number (0-99): ".format(i)))
            if jersey_num < 0 or jersey_num > 99:
                raise ValueError("Invalid jersey number, please enter a number between 0 and 99.")
            
            pts = int(input("Enter points scored for player {}: ".format(i)))
            fga = int(input("Enter field goals attempted for player {}: ".format(i)))
            fta = int(input("Enter free throws attempted for player {}: ".format(i)))
            to = int(input("Enter turnovers committed by player {}: ".format(i)))
            
            #STEP 4: Calculate their ppp value based on the information provided.  
            
            ppp = pts / (fga + (0.44 * fta) + to)
            pos_efficiency[ppp] = jersey_num
            
            break  
        
        #STEP 5: Display the error in case of incorrect inputs.
        
        except ValueError as e:
            print(e)  
            continue  

#STEP 6: Sort the roster based on PPP and display the full report.            
            
sorted_roster = sorted(pos_efficiency.items(), reverse=True)

print()
for ppp, jersey_num in sorted_roster:
    rounded_ppp = round(ppp, 2)
    print("Jersey number: {}, Points per Possession: {}".format(jersey_num, rounded_ppp))
