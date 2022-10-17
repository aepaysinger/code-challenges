# TRY WITH ONE FUNCTION!
# Rules: start with 11 players, red card lose 1 player, 2 yellow cards lost 1 player,
# must have 7 or more players
def football_cards(team_cards):
    a_card, b_card = check_card(team_cards)
    a_players = 11
    b_players = 11
    while a_players or b_players != 6:#fix
        # for player in a_card:
        #     if a_card[player] == "YY":
        #         a_players -= 1
        #     if a_card[player] == "R":
        #         a_players -= 1
        #     if b_card[player] == "YY":
        #         b_players -= 1
        #     if b_card[player] == "R":
        #         b_players -= 1
        for i in range(10):
            if a_card[i+1] == "YY":
                a_players -= 1
            if a_card[i+1] == "R":
                a_players -= 1
            if b_card[i+1] == "YY":
                b_players -= 1
            if b_card[i+1] == "R":
                b_players -= 1
            

        
    return (a_players, b_players)
    

    
def check_card(team_cards):
    a_team = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
        11: ""
    }
    b_team = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
        11: ""
    }
    for card in team_cards:
        if card[0] == "A":
            if len(card) == 3:
                a_team[int(card[1])] += card[2]
            else:
                card_num = card[1] + card[2]
                a_team[int(card_num)] += card[3]
        else:
            if len(card) == 3:
                b_team[int(card[1])] += card[2]
            else:
                card_num = card[1] + card[2]
                b_team[int(card_num)] += card[3]
    return a_team, b_team




if __name__ == "__main__":
    team_cards = ["A4Y", "A4Y"]
    print(football_cards(team_cards))