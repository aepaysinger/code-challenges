import re


def football_cards(team_cards):
    leave_field = {"R", "YY", "YR"}
    teams = {
        "A": {"players": 11, "cards": {}},
        "B": {"players": 11, "cards": {}},
    }

    for card in team_cards:
        if teams["A"]["players"] == 6 or teams["B"]["players"] == 6:
            break
        match = re.match(r"([AB])([0-9]+)([YR])", card)
        team, player, penalty = match.groups()
        teams[team]["cards"][player] = teams[team]["cards"].get(player, "") + penalty
        if teams[team]["cards"][player] in leave_field:
            teams[team]["players"] -= 1
    return (teams["A"]["players"], teams["B"]["players"])


if __name__ == "__main__":
    team_cards = ["A4R", "A6Y", "A8R", "A10R", "A11R"]
    print(football_cards(team_cards))
