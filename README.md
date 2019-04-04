# web-scraper
Generic tool to index search results. Written in Python using Beautiful Soup. Analyzes sentiment and subjectivity of search results using polarity metric.

## Required packages

1. textblob

2. bs4

3. requests

## Sentiment and subjectivity

Useful to determine the psychological influence indexed search results may have.

## Example Run

````
example = Analysis('spacex')
example.run()
print(example.term, 'Subjectivity: ', example.subjectivity, 'Sentiment: ', example.sentiment)
````
