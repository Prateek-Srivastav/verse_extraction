import requests
import re
import json

# link to fetch data from
link = 'https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext/sa_aSTAvakragItA.txt'

response = requests.get(link)
text = response.text

# verses and index are after the '# Text', so splitting on it
# second split is for getting each verse individually, as they are separated by '\n\n', therefore using it to split
gita_verses = text.split('# Text')[1].split('\n\n')[2:]

# regex pattern for extracting numbers from a text with decimal
decimal_pattern = r'\b\d+\.\d+\b'

# list to store the verses
extracted_shlokas = []
# looping over all the verses
for verse in gita_verses:
    # index is after the '//', so splitting on it
    splitted = verse.split('//')
    extracted_shlokas.append({
        "verse": splitted[0].strip(), # first index is verse, stripping to remove all whitespaces
        "index": re.findall(decimal_pattern, splitted[1].split('_')[1])[0] # extracting only the numbers, ignoring other texts like '\n'
    })

# converting python dict to json
json_data = json.dumps(extracted_shlokas, ensure_ascii=False, indent=2)

# saving to json file
with open("astavakra_gita_verses.json", "w", encoding="utf-8") as file:
    file.write(json_data)
