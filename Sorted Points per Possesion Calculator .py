pos_efficiency = {}

i = 1

for i in range (1,13):
    jersey_num = int(input("Enter player {}'s jersey number:\n".format(i)))
    PTS = int(input('Enter points scored for player {}: '.format(i)))
    FGA = int(input('Enter field goals attempted for player {}: '.format(i)))
    FTA = int(input('Enter free throws attempted for player {}: '.format(i)))
    TO = int(input('Enter turnovers committed by player {}: '.format(i)))
    PPP = PTS/(FGA + (0.44 * FTA) + TO)

    if jersey_num < 0 or jersey_num > 99:
        break
    else:
        pos_efficiency[PPP] = jersey_num



sorted_roster = sorted(pos_efficiency.items(), reverse = True)

print()
for PPP, jersey_num in sorted_roster:

    rounded_PPP = round(PPP,2) 

    print('Jersey number: {}, Points per Possession: {}'.format(jersey_num, rounded_PPP))

