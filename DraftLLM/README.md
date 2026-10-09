# Draft LLM
## Tokenizer.py
Tokenizer.py is a simple tokenizer desinged to encode the entire league.txt file (or any other .txt file) into tokens that store the data. Then the decoder uses these tokens and decodes them back into the reference text to be output as the original text.
### This works in a couple simple ways
- First the text is prepared for the enoder by being stripped of all spaces and special charachters such as a question mark period or comma.
- Next the encoder converts the text into computer readable tokens unique to each word 
- Using these it stores them in its library of tokens
- Then later on in the program it decodes the token and essentially undoes the encoding process in order to spit out the original text

## TokenizerInteractive.py

TokenizerInteractive.py works very similarly to Tokenizer.py the only difference being the fact unlike Tokenizer.py you can input text into the Tokenizer to check it against the database of text it already has to confirm or deny wether it exists.
### This works quite simply as well
- First it prompts the user for an input of some text tht the user wants to check if it exists within its library
- Then it will encode the users input to check its token against its library
- If a matching text is found it will pint that the text was found