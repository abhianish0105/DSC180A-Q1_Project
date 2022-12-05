# Twitter Sentiment Toward Remote Work During COVID-19

This is a data analysis project and machine learning project that live-streams real-time tweets from Twitter to analyze their sentiment.

![GoalArchitecturePic](https://user-images.githubusercontent.com/77038831/205740810-db44be83-8df8-4f6c-8314-319f381062e4.png)

### 'producer_test.py' 
This file contains the code for producing the raw tweets using Twitter API, and sends them to our input topic to be fed into our function.

### 'function_test.py'
This file contains the code that reads the raw tweets from the input topic, applies further preprocessing, and sends the filtered tweets to the output topic.

### 'consumer_test.py'
This file contains the code which receives the filtered tweets from the output topic, applies sentiment analysis, and outputs these files to a CSV which shows the counts of each sentiment received.

### 'test.py'
This file contains the code for initializing the consumer and the pipeline, which starts the stream of tweets from the Twitter API.

## Group Members
- Brandon Vinhnee
- Abhishek Nisha Anish
- Tej Patel
