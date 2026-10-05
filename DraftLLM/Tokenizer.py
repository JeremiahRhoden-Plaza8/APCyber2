import re #regex expressions

source_file = 'league.txt'

# Read a sample of the text
with open(source_file, "r", encoding ="utf-8") as file;
    raw_text = file.read()
print("Toltal number of characters: ", len(raw_text))