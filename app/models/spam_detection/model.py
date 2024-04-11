import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

class SpamDetection():
  def __init__(self):
    self.model_path = 'app/models/spam_detection/trained_model.pkl'
    self.setup()
    self.load_model()

  def setup(self):
    df = pd.read_csv('app/models/spam_detection/traindata.csv')
    df = df.where((pd.notnull(df)), '')
    df.loc[df['Category'] == 'spam', 'Category'] = 0
    df.loc[df['Category'] == 'ham', 'Category'] = 1
    X = df['Message']
    Y = df['Category']
    X_train, _, Y_train, _ = train_test_split(
        X, Y, test_size=0.2, random_state=3)
    self.feature_extraction = TfidfVectorizer(
        min_df=1, stop_words='english', lowercase=True)
    self.X_train_features = self.feature_extraction.fit_transform(X_train)
    self.Y_train = Y_train.astype('int')

  def load_model(self):
    try:
        self.model = joblib.load(self.model_path)
    except FileNotFoundError:
        self.train_model()

  def train_model(self):
    self.model = LogisticRegression()
    self.model.fit(self.X_train_features, self.Y_train)
    joblib.dump(self.model, self.model_path)

  def is_spam(self, review):
      review = [review]
      input_features = self.feature_extraction.transform(review)
      prediction = self.model.predict(input_features)
      return False if prediction[0] == 1 else True