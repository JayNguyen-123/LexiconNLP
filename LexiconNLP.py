import nltk
from nltk.corpus import opinion_lexicon

def analyze_sentiment(text):
    positive_words = set(opinion_lexicon.positive())
    negative_words = set(opinion_lexicon.negative())

    # tokenizer the input text into individual words
    tokens = nltk.word_tokenize(text)

    # count the number of positive and negative words in the text
    positive_counts = sum(1 for word in tokens if word in positive_words)
    negative_counts = sum(1 for word in tokens if word in negative_words)

    # determine sentiment based on the words counts
    if positive_counts > negative_counts:
        sentiment = "Positve"
    elif positive_counts < negative_counts:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

text = " I really enjoy the movie. It was fantastic!"
sentiment = analyze_sentiment(text)

print("Sentiment: ", sentiment)
