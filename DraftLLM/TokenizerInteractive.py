import re #regex expressions

source_file = 'words.txt'

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
# Now lets build a Tokenizer 
class SimpleTokenizerV1:
    #Create a constructor for simpleTokenizerV1
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    #Encode: create set of token ids
    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    #Decode: given token ids, create corresponding text
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?_!"()\'])', r'\1', text)
        return text
    #Create new tokenizer object
tokenizer = SimpleTokenizerV1(vocab)
user_word = input("Enter a chosen word: ")
text = user_word

#Encode the text sample
ids = tokenizer.encode(text)
print(ids)\

#Decode the token ids
final_text = tokenizer.decode(ids)
print(final_text)

#end of text & unknown tokens
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

#rebuild vocab to account for unknown
vocab = {token:integer for integer,token in enumerate(all_tokens)}

#length of vocab
len(vocab.items())

#explore sample
for i, item in enumerate(list(vocab.items())[-5:]):
    print(item)

#tokenizer V2
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = { i:s for s,i in vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        #Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text

#use SimpleTokenizerV2
tokenizer = SimpleTokenizerV2(vocab)

text1 = "long object, spindle-shaped, occasionally phosphorescent" 
text2 = "Not to mention rumours which agitated the maritime population"
text3 = "My name is Jeremiah"

text = " <|endoftext|> ".join((text1, text2))
new_text = " <|endoftext|> ".join((text1, text3))

print(text)
print(new_text)