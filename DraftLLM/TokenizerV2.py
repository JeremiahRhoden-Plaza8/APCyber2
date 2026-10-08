import re #regex expressions

source_file = 'data.txt'

# Read a sample of the text
with open(source_file, "r", encoding="utf-8") as file:
    raw_text = file.read()
print("Total number of characters: ", len(raw_text))

#View sample
print(raw_text[:60])

#Strip whitespace from text:
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))

#View all words
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

#Create a vocabulary
vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

#Now let's build a tokenizer
class SimpleTokenizerV1:
    #Create constructor for SimpleTokenizerV1
    def __init__(self, vocab):
        self.str_to_int = vocab           
        self.int_to_str = {i:s for s,i in vocab.items()}

    # Encode: create set of token ids
    def encode(self, text):        
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    #Decode: Given token ids, create corresponding text
    def decode(self, ids):        
        text = " ".join([self.int_to_str[i] for i in ids]) 
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)   
        return text

#Create new tokenizer object
tokenizer = SimpleTokenizerV1(vocab)
text = """This is a Mets year,for all you Mets here. Let’s go! Let’s go Mets!"""


#Encode the text sample
ids = tokenizer.encode(text)
print(ids)
 # output: [5,6,4,7,190,8]

#Decode the token ids 
final_text = tokenizer.decode(ids)
print(final_text)

# Add end of text and unknown tokens
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

#Rebuild the vocabulary to include those new tokens
vocab = {token:integer for integer,token in enumerate(all_tokens)}

#Get length of vocabulary
len(vocab.items())

# Explore sample
for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)

#Rebuild SimpleTokenizer
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = { i:s for s,i in vocab.items()}

    def encode(self, text):
            preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
            preprocessed = [item.strip() for item in preprocessed if item.strip()]
            preprocessed = [
                item if item in self.str_to_int 
                else "<|unk|>" for item in preprocessed
            ]

            ids = [self.str_to_int[s] for s in preprocessed]
            return ids

    def decode(self, ids):
            text = " ".join([self.int_to_str[i] for i in ids])
            # Replace spaces before the specified punctuations
            text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
            return text

text1 = "There’s no stopping us now, we’re gonna do it again."
text2 = "Do it, (do it) do it, (do it) do it, let’s go! Ohh…"
text3 = "This is a Mets year,for all you Mets here. Let’s go! Let’s go Mets!" 

text = " <|endoftext|> ".join((text1, text2))
new_text = " <|endoftext|> ".join((text1, text3))

print(text)
print(new_text)
lyrics = input("Are you a real Mets Fan name a player from the 1986 championship team: ")

#Encode the text sample
ids = tokenizer.encode(lyrics)
print(ids)\

#Decode the token ids
final_text = tokenizer.decode(ids)
print(final_text + " was a fantastic player you must be a real fan!")

#Use SimpleTokenizerV2 
tokenizer = SimpleTokenizerV2(vocab)

#Encode
print(tokenizer.encode(text))

#Decode
print(tokenizer.decode(tokenizer.encode(text)))


#Encode
print(tokenizer.encode(new_text))

#Decode
print(tokenizer.decode(tokenizer.encode(new_text)))