# rollbert
A discord bot that serve as a "dice rolling" system from Dungeons &amp; Dragons 5e. The bot also allows users to search the dnd5e SRD api to find spell descriptions and mechanics.

## commands
#### !roll 
>* !roll: with no other arguments will generate a number between 1-20, to simulate rolling a 20-sided die
>* !roll d#: will generate a number between 1-#. The number must be one that is typically found in a dungeons and dragons (d4, d6, d8, d10, d12, d20, d100)
>* !roll # d#: will generate however many rolls specified in the second argument, list them and list the total.

#### !spell "spell name"
>* search the dnd5eSRD api for spell descriptions and returns it to the discord channel
