##### Global Variables ####
teamRoster = {}
##### Functions #####
# HINT: see figure 8.28.2
def outputRoster():
    print ("ROSTER")
    for jerseyNumber in sorted(teamRoster.keys() ):
        print (f"Jersey number: {jerseyNumber}, Rating: {teamRoster[jerseyNumber]}")
    print()
def addPlayer():
    try:
        jerseyNumber = int(input("Enter a new player's jersey number:\n"))
        teamRoster[jerseyNumber] = int(input("Enter the player's rating:\n"))
    except ValueError:
        print('Input is not an integer. Please input an integer')
    else:
        print('The player number and rating has been added.')
    print()    
def deletePlayer():
    try:
        jerseyNumber = int(input("Enter a jersey number:\n"))
        teamRoster.pop(jerseyNumber)
    except KeyError:
        print('Invalid jersey number. Please enter a valid jersey number.')
    else:
        print('The player has been deleted.')
    print()
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
# Input 5 players
for i in range(1,6):
    jerseyNumber = int(input(f"Enter player {i}'s jersey number:\n") )
    teamRoster[jerseyNumber] = int(input(f"Enter player {i}'s rating:\n") )
    print ()
outputRoster()

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
    
