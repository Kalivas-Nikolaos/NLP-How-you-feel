# main.py
import sys
import requests
import json
import pandas as pd 
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
     
length = len(sys.argv)

key_word = str(sys.argv[2])
url = ('https://newsapi.org/v2/everything?'
	'q='+key_word+'&'
	'from=2021-11-23&'
	'sortBy=popularity&'
	'apiKey=3ae56a09c6ba40bd98fc534f7b83cc3c')

r = requests.get(url).json()

if length==3 : #argument 2 
	print('Status is' , r['status'],'\nTotal Result is' , 	r['totalResults'], '\nThe Most popular article : ', 		r['articles'][0])

df = pd.json_normalize(r['articles'])	
df['title'] = df['title'].astype('string')#convert all titles 
sql_string = ""                          # into a single string.
sentences = tuple(df.title.tolist())
text = sql_string + str(sentences)	
		
# function to print sentiments of the sentence.
def sentiment_scores(text):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
 
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(text)
     
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% 			Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% 			Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% 	Positive")
 
    print("Sentence Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
 
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
 
    else :
        print("Neutral")
	
if length==4 and sys.argv[3] == 'sentiment' :
	sentiment_scores(text)
	
if length==5 and sys.argv[4] == 'methodA' :
	testimonial = TextBlob(text) # call sentiment method from 		TextBlob
	sentiment_dict = testimonial.sentiment
	print(testimonial.sentiment) # print the sentiment results
	if sentiment_dict.polarity > 0.2 and 			   		sentiment_dict.subjectivity <0.5 :
  		print('positive')
	else:
  		print('negative')
	


        
