import re
def football_cards(team_cards):
    a_players = 11
    b_players = 11
    a_cards = {}
    b_cards = {}

    for card in team_cards:
        match = re.match(r"([AB])([0-9]+)([YR])", card)
        team, player, penalty = match.groups()
        print(team, player, penalty)

    
    # for card in team_cards:
    #     if a_players == 6 or b_players == 6:
    #         break
    #     if card[0] == "A":
    #         if len(card) == 3:
    #             player_number = card[1]
    #             a_cards[player_number] = a_cards.get(player_number, "") + card[2]
    #             if (
    #                 a_cards[player_number] == "R"
    #                 or a_cards[player_number] == "YY"
    #                 or a_cards[player_number] == "YR"
    #                 ):
    #                 a_players -= 1
    #         else:
    #             player_number = card[1] + card[2]
    #             a_cards[player_number] = a_cards.get(player_number, "") + card[3]
    #             if (
    #                 a_cards[player_number] == "R"
    #                 or a_cards[player_number] == "YY"
    #                 or a_cards[player_number] == "YR"
    #             ):
    #                 a_players -= 1
    #     else:
    #         if len(card) == 3:
    #             player_number = card[1]
    #             b_cards[player_number] = b_cards.get(player_number, "") + card[2]
    #             if (
    #                 b_cards[player_number] == "R"
    #                 or b_cards[player_number] == "YY"
    #                 or b_cards[player_number] == "YR"
    #                 ):
    #                 b_players -= 1
    #         else:
    #             player_number = card[1] + card[2]
    #             b_cards[player_number] = b_cards.get(player_number, "") + card[3]
    #             if (
    #                 b_cards[player_number] == "R"
    #                 or b_cards[player_number] == "YY"
    #                 or b_cards[player_number] == "YR"
    #                 ):
    #                 b_players -= 1
    # return (a_players, b_players)

    


if __name__ == "__main__":
    team_cards = ["A4R", "A6R", "A8R", "A10R", "A11R"]
    print(football_cards(team_cards))
