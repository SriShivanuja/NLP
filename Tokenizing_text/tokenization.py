import nltk
from nltk.tokenize import word_tokenize
def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens
sample_inputs = [
"Tokenization is the process of dividing a text into smaller units known as tokens",
"Tokenization is an important NLP task.",
]
for input_text in sample_inputs:
    print("Input:", input_text)
    tokens = tokenize_text(input_text)
    print("Tokens:", tokens)
    print()
