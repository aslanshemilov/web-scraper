from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

#Author: Shilpa Kancharla

class Analysis:
    def __init__(self, term):
        self.term = term #search term
        #The following variables are for analyzing the sentiment
        self.subjectivity = 0
        self.sentiment = 0
        #0 in brackets will be replaced by our request
        #For now, 'nws' stands for news, but we can change this later
        self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)

    def run(self):
        response = requests.get(self.url)
        print(response.text) #Prints to console
        #Use html parse to parse text
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_results = soup.find_all('div', class_='st')
        for h in headline_results:
            print(h) #Print out all the headlines
            blob = TextBlob(h.get_text())
            #Polarity value is between -1 and 1.
            #Represents whether we have a negative or positive sentiment expressed,
            #respectively. We also analyze subjectivity.
            #Divide by number of results to get an average metric.
            self.sentiment += blob.sentiment.polarity / len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity / len(headline_results)

#Example run
example = Analysis('spacex')
example.run()
print(example.term, 'Subjectivity: ', example.subjectivity, 'Sentiment: ', example.sentiment)
