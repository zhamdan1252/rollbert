import random

def roll(messageContents):
    diceTypes = ["d100", "d20", "d12", "d10", "d8", "d6", "d4"]
    parsed = messageContents.split(" ")

    if len(parsed) == 1:
        response = f'You rolled: {random.randint(1,20)}'
        return response

    elif len(parsed) == 2:

        if parsed[1] in diceTypes:
            dieValue = int(parsed[1].replace("d", ""))
            response = f'You rolled: {random.randint(1, dieValue)}'
            return response

        response = 'Did not recognize a dice type. Use the format \'!roll d##\' to specify dice type. If rolling multiple dice, use this format: \'!roll # d##\'.'
        return response
    elif len(parsed) > 2:
        if parsed[1].isnumeric() and parsed[2] in diceTypes:
            numOfDice = int(parsed[1])

            if(numOfDice > 100):
                response = '...There\'s no reason you need to roll that much...'
                return response

            dieValue = int(parsed[2].replace("d", ""))
            rolls = [random.randint(1, dieValue) for _ in range(numOfDice)]

            response = f'You Rolled: {", ".join(map(str, rolls))}\n Total: {sum(rolls)}'
            return response

    response = "Did not recognize format. Use the format \'!roll d##\' to specify dice type. If rolling multiple dice, use this format: \'!roll # d##\'."
    return response