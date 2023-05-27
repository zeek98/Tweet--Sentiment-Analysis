# Tweet--Sentiment-Analysis
Sentiment analysis of tweets based on excel files.

We would analyse tweets based on a excel file as the data was already collected in advance.

In this code, we start by importing the necessary libraries, including pandas for data manipulation, nltk for natural language processing, SentimentIntensityAnalyzer for sentiment analysis, stopwords for removing common words, word_tokenize for tokenization, and re for regular expressions.

We then download the required NLTK resources (vader_lexicon, stopwords, and punkt) using the nltk.download() function.

The CSV file containing the Twitter data is loaded into a pandas DataFrame using pd.read_csv().

Next, we initialize the sentiment analyzer using SentimentIntensityAnalyzer().

To preprocess the tweets, we define a function called preprocess_tweet(). This function converts the tweet to lowercase, removes URLs using regular expressions, eliminates special characters and numbers, tokenizes the tweet, removes stopwords using the NLTK stopwords corpus, and finally joins the tokens back into a single string.

We apply the preprocess_tweet() function to the 'text' column of the DataFrame and store the cleaned tweets in a new column called 'cleaned_text'.

Sentiment analysis is performed using the SentimentIntensityAnalyzer on the 'cleaned_text' column, and the compound sentiment score is calculated for each cleaned tweet. The sentiment scores are added to a new column called 'sentiment' in the DataFrame.

Finally, we analyze the sentiment results by filtering the DataFrame based on positive, negative, and neutral sentiments. The sentiment distribution is printed to the console, displaying the number of positive, negative, and neutral tweets.





