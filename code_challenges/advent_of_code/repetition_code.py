def get_messages():
    with open("./code_challenges/advent_of_code/message_input") as message_input:
        messages = message_input.read().split("\n")
    return messages


def break_up_messages():
    messages = get_messages()
    character_breakdown = []

    for message in messages:
        for i, character in enumerate(message):
            while len(character_breakdown) < len(messages[0]):
                character_breakdown.append({})
            character_breakdown[i][character] = (
                character_breakdown[i].get(character, 0) + 1
            )
    return character_breakdown


def find_hidden_message_high():
    character_breakdown = break_up_messages()

    hidden_message = ""
    for characters in character_breakdown:
        hidden_message += max(characters, key=lambda character: characters[character])
    return hidden_message


def find_hidden_message_low():
    character_breakdown = break_up_messages()

    hidden_message = ""
    for characters in character_breakdown:
        hidden_message += min(characters, key=lambda character: characters[character])

    return hidden_message
