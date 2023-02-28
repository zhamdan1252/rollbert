import requests
import json

def getSpell(userSubmittedSpell):

    spells = requests.get('https://www.dnd5eapi.co/api/spells')
    spell_list = json.loads(spells.text)
    print(spell_list['results'])

    for s in spell_list['results']:
        if (s['index'] == userSubmittedSpell):
            spellJson = f'https://www.dnd5eapi.co/api/spells/{userSubmittedSpell}'
            spellFound = requests.get(spellJson)
            spellInfo = json.loads(spellFound.text)
            spellDesc = spellInfo.get('name') + " (level " + str(spellInfo.get('level')) + " " + spellInfo['school'].get('name') + "):\n\nRange: " + spellInfo.get('range') + "\n\nComponents: " + " ".join(map(str, spellInfo.get('components')))
            if 'material' in spellInfo:
                spellDesc +=  "\n\nMaterials: " + "".join(map(str, spellInfo.get('material')))

            spellDesc += "\n\nCasting Time: " + spellInfo.get('casting_time')
            if (spellInfo.get('ritual')):
                spellDesc += " [RITUAL]"

            spellDesc += "\n\nDuration: " + spellInfo.get('duration') + "\n\nConcentration: "
            if spellInfo.get('concentration'):
                spellDesc += "yes"
            else:
                spellDesc += "no"
            spellDesc += "\n\nDescription: " + "".join(map(str,spellInfo.get('desc')))

            if len(spellInfo.get('higher_level')) > 0:
                spellDesc += "\n\nHigher Level: " + "".join(map(str,spellInfo.get('higher_level')))

            return spellDesc;

    return "Spell not found."