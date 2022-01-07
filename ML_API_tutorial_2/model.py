# ML imports
# from sklearn.ensemble import RandomForestClassifier
import pickle

# from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# spacy_tok


class ml_model():

    def __init__(self):
        """Aggregate random forest and linear regression prediction model
        Attributes:
            rfr: sklearn random forest regression model
            lp: sklearn linear regression model
        """

        rf_filename = 'rf_model'
        lr_filename = 'lr_model'
        loaded_rf_model = pickle.load(open(rf_filename, 'rb'))
        loaded_lr_model = pickle.load(open(lr_filename, 'rb'))
        self.rfr = ''
        self.lp = ''
        self.model = MultinomialNB()
        # self.vectorizer = TfidfVectorizer(tokenizer=spacy_tok)
        self.vectorizer = TfidfVectorizer()

    def vectorizer_fit(self, X):
        """Fits a TFIDF vectorizer to the text
        """
        self.vectorizer.fit(X)

