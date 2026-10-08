import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load sample data (reviews.csv with a column 'review')
data = pd.read_csv("reviews.csv")

# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Apply function
data['Sentiment'] = data['review'].apply(get_sentiment)

# Count sentiments
sentiment_counts = data['Sentiment'].value_counts()

# Plot
plt.figure(figsize=(6,6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['blue', 'green', 'red'])
plt.title("Sentiment Analysis Results")
plt.savefig("output.png")
plt.show()
