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
    jerseyNumber = int(input("Enter a new player's jersey number:\n"))
    teamRoster[jerseyNumber] = int(input("Enter the player's rating:\n"))
    print()
def deletePlayer():
    jerseyNumber = int(input("Enter a jersey number:\n"))
    teamRoster.pop(jerseyNumber)
    print()
def updatePlayerRating():
    jerseyNumber = int(input("Enter a jersey number:\n"))
    teamRoster[jerseyNumber] = int(input("Enter a new rating for player:\n"))
    print()
def outputPlayersAboveRating():
    givenRating = int(input("Enter a rating:\n") )
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
    
