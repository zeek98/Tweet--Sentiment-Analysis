# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qgya6O8PyZ3uawLX_YvzAtr4dghgJikO
"""

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Download necessary NLTK resources
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')

# Load CSV file into a pandas DataFrame
data = pd.read_csv('twitter_data.csv')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Preprocess function to clean the tweets
def preprocess_tweet(tweet):
    # Convert tweet to lowercase
    tweet = tweet.lower()
    
    # Remove URLs from tweet
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    
    # Remove special characters and numbers from tweet
    tweet = re.sub(r"[^\w\s]", '', tweet)
    tweet = re.sub(r"\d+", '', tweet)
    
    # Tokenize the tweet
    tokens = word_tokenize(tweet)
    
    # Remove stopwords from tweet
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Join the tokens back into a single string
    preprocessed_tweet = ' '.join(filtered_tokens)
    
    return preprocessed_tweet

# Apply preprocessing to the 'text' column of DataFrame
data['cleaned_text'] = data['text'].apply(preprocess_tweet)

# Perform sentiment analysis and add results to DataFrame
data['sentiment'] = data['cleaned_text'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Analyze the sentiment results
positive_tweets = data[data['sentiment'] > 0]
negative_tweets = data[data['sentiment'] < 0]
neutral_tweets = data[data['sentiment'] == 0]

# Print the sentiment distribution
print("Sentiment Distribution:")
print("Positive Tweets:", len(positive_tweets))
print("Negative Tweets:", len(negative_tweets))
print("Neutral Tweets:", len(neutral_tweets))