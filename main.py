# Requirement: Make a program which effectively simulates a team management system.

# Solution: A series of functions which allows the user to create their own team roster with a rating system.

teamRoster = {}
##### Functions #####

# Function 1: Displays roster to the user.

def outputRoster():
    print ("ROSTER")
    for jerseyNumber in sorted(teamRoster.keys() ):
        print (f"Jersey number: {jerseyNumber}, Rating: {teamRoster[jerseyNumber]}")
    print()

# Function 2: Adds a player to the roster.    
    
def addPlayer():
    try:
        jerseyNumber = int(input("Enter a new player's jersey number:\n"))
        teamRoster[jerseyNumber] = int(input("Enter the player's rating:\n"))
    except ValueError:
        print('Input is not an integer. Please input an integer')
    else:
        print('The player number and rating has been added.')
    print() 

# Function 3: Deletes a player from the roster.    
    
def deletePlayer():
    try:
        jerseyNumber = int(input("Enter a jersey number:\n"))
        teamRoster.pop(jerseyNumber)
    except KeyError:
        print('Invalid jersey number. Please enter a valid jersey number.')
    else:
        print('The player has been deleted.')
    print()
    
# Function 4: Enables user to update an existing player's rating

def updatePlayerRating():
    try:
        jerseyNumber = int(input("Enter a jersey number:\n"))
        teamRoster[jerseyNumber] = int(input("Enter a new rating for player:\n"))
    except ValueError:
        print('Input is not an integer. Please input an integer.')
    except KeyError:
        print('Invalid jersey number. Please enter a valid jersey number')
    else:
        print('The player rating has been updated.')
    print()

# Function 5: Allows user to see which players have a rating greater than a given value.    
    
def outputPlayersAboveRating():
    try:
        givenRating = int(input("Enter a rating:\n") )
    except ValueError:
        print('Input is not an integer. Please input an integer.')
        return    
    print()
    print ("ABOVE",givenRating)
    for jerseyNumber in sorted(teamRoster.keys() ):
        if teamRoster[jerseyNumber] > givenRating:
            print (f"Jersey number: {str(jerseyNumber)}, Rating: {str(teamRoster[jerseyNumber])}" )
    print()
    
################  MAIN  ########################    

# Program begins by asking the user to input 5 players which is followed by a menu where the user can utilize the functions above.

for i in range(1,6):
    jerseyNumber = int(input(f"Enter player {i}'s jersey number:\n") )
    teamRoster[jerseyNumber] = int(input(f"Enter player {i}'s rating:\n") )
    print ()
outputRoster()

# Displays the menu options.

menu =\
'''MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
'''
option = ''

# Statements that run based on the input.

while True:
    print (menu)
    option = input("Choose an option:\n")
    if option == 'q':
        break
    if option == 'a':
        addPlayer()
        continue
    if option == 'd':
        deletePlayer()
        continue
    if option == 'u':
        updatePlayerRating()
        continue
    if option == 'r':
        outputPlayersAboveRating()
        continue
    if option == 'o':
        outputRoster()
        continue
    else:
        print('Invalid option. Please input a key based on the menu.')
    
