# amazon-review-datascrap-and-sentiment-python
Scrap amazon reviews and do sentiment analysis on them


## To achieve the problem statement, I have followed the following steps:

### Step 1:
I need to parse the data (product review) from the given website, so I used the BeautifulSoup library in python to achieve this. You can find my code in the file named *amazon-scrap-LIVE-v2* .
After scraping the data, I used pandas library to convert the parsed dictionary into dataframe for simplicity and easy data management
Then used NLTK library to preprocess the parsed data:
Removed stopwords
Used regex to remove unwanted punctuations 
from the review text

### Step 2:
Next I did sentiment analysis for better understanding of the parsed reviews 
To achieve this, I used the **TextBlob** and  **Vader** libraries which were pretty straight forward. 
We get output from **TextBlob** as **polarity** and **subjectivity** whose values are between -1 and +1
From “Vader” we get *negative*, *neutral* and *positive* confidence whose values are between 1 and 0

### Step 3:
No I need to store this data-frame into table/database so I used sqlite v3 because well it's simple and easy to use + it portable 
I achieved this using the library sqlite3 in python. 
The name of the database is *amz_reviewsv1.db* and the table is *iphone12_reviews_v1*, I have included the db in the submission folder 

### Step 4:
Now, for creating the API, I iused the Flask framework. The statement of this API is to get sentiment from any new given reviews
Here also I have used **TextBlob** and **Vader** libraries to get the  sentiment of the review
The name of the file is *app.py* which can be found in the submission folder

### Steps to run the code: 
```python
> Create a virtual environment, activate it

> Run “pip install -r requirements.txt” to install all the dependencies

> Since to achieve Step 1, 2 and 3, I have used jupyter notebook, run the command : Jupyter notebook amazon-scrap-LIVE-v2.ipynb

> Now to run the flask api, run the command: Python app.py
```

*Thank you*
**Gourab Dasgupta**
