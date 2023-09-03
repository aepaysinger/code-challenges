def get_messages():
    with open("./code_challenges/advent_of_code/message_input") as message_input:
        messages = message_input.read().split("\n")
    return messages


def break_up_messages():
    messages = get_messages()
    character_breakdown = {}
    for i in range(len(messages[0])):
        character_breakdown[f"position {str(i)}"] = {}

    for message in messages:
        for i, character in enumerate(message):
            character_breakdown[f"position {str(i)}"][character] = (
                character_breakdown[f"position {str(i)}"].get(character, 0) + 1
            )
    return character_breakdown


def find_hidden_message_high():
    character_breakdown = break_up_messages()

    hidden_message = ""
    for position, characters in character_breakdown.items():
        highest_character = None
        highest_count = 0
        for character, count in characters.items():
            if count > highest_count:
                highest_character = character
                highest_count = count
        hidden_message += highest_character

    return hidden_message


def find_hidden_message_low():
    character_breakdown = break_up_messages()

    hidden_message = ""
    for characters in character_breakdown.values():
        lowest_character = None
        lowest_count = float("inf")
        for character, count in characters.items():
            if count < lowest_count:
                lowest_character = character
                lowest_count = count
        hidden_message += lowest_character

    return hidden_message
