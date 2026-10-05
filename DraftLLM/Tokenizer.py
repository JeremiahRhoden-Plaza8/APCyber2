import re #regex expressions

source_file = 'league.txt'

# Read a sample of the text
with open(source_file, "r", encoding ="utf-8") as file:
    raw_text = file.read()
print("Toltal number of characters: ", len(raw_text))

#View sample
print(raw_text[:60])

#Strip whitespace from text
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))

#View all words
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)
print(all_words [:20])

#Map tokens w/ ids
vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break