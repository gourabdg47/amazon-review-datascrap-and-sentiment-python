from flask import *

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# import nltk
# from nltk.corpus import stopwords
# nltk.download('stopwords')
# from nltk.tokenize import word_tokenize

app = Flask(__name__)

# def stopword_removal(review_text):
#     stop_words = set(stopwords.words('english'))
#     word_tokens = word_tokenize(review_text)
#     filtered_sentence = [w for w in word_tokens if not w in stop_words]
#     filtered_sentence = [w for w in word_tokens if w not in stop_words]
#     return filtered_sentence

def TextBlob_sentiment(review_text):
    analysis = TextBlob(review_text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

def VADER_sentiment(review_text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(review_text)

@app.route("/review-sentiment", methods=["POST"])
def review_sentiment():
    
    amz_review = request.data
    req_data = amz_review.decode('utf-8')
    data = json.loads(req_data)
    
    ### TextBlob sentiment ########
    
    polarity, subjectivity = TextBlob_sentiment(data['review'])
    
    textblob_dict = {
        "TextBlob" : {
            'polarity' : polarity,
            "subjectivity" : subjectivity
        }
    }
    
    data.update(textblob_dict)
    
    ##############################@
    
    ##### VADER sentiment #####
    
    vader_senti = VADER_sentiment(data['review'])
    
    VADER_dict = {
        "VADER" : vader_senti
    }
    
    data.update(VADER_dict)
    
    ############################
    
    
    # print(stopword_removal(data['review']))
    
    return data
    

if __name__ == '__main__':  
   
    app.run(host='0.0.0.0', port = 8081, debug = True)