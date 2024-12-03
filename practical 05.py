import nltk
nltk.download('punkt')
print(nltk.data.path)
from nltk.tokenize import sent_tokenize, word_tokenize
# Sample text
Txt = "Good Day Mr. Vermeulen, how are you doing today? The weather is great, and Data Science is awesome. You are doing well!"
# Tokenize the text into sentences
print("Identify sentences")
print(sent_tokenize(Txt), '\n')
# Tokenize the text into words
print("Identify words")
print(word_tokenize(Txt))
