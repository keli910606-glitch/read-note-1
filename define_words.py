import requests

def get_definition_and_example(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        definition = data['meanings'][0]['definitions'][0]['definition']
        example = data['meanings'][0]['definitions'][0].get('example', 'No example available.')
        return definition, example
    else:
        return "Definition not found.", "No example available."
# Read words from file
with open("vocabulary.txt", "r") as file:
    words = [line.strip() for line in file]

# Write results to new file
with open("vocabulary_definitions.md", "w") as output:
    for word in words:
        definition, example = get_definition_and_example(word)
        output.write(f"### {word}\n")
        output.write(f"- **Definition**: {definition}\n")
        output.write(f"- **Example**: {example}\n\n")
