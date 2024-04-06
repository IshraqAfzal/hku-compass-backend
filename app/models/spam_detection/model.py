import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

class SpamDetection():
  def __init__(self) -> None:
    self.model_path = './trained_model.pkl'
    try:
        self.model = joblib.load(self.model_path)
    except FileNotFoundError:
        self.train_model()

  def train_model(self):
    df = pd.read_csv('./traindata.csv')
    df = df.where((pd.notnull(df)), '')
    df.loc[df['Category'] == 'spam', 'Category'] = 0
    df.loc[df['Category'] == 'ham', 'Category'] = 1

    X = df['Message']
    Y = df['Category']
    X_train, _, Y_train, _ = train_test_split(
        X, Y, test_size=0.2, random_state=3)
    
    self.feature_extraction = TfidfVectorizer(
        min_df=1, stop_words='english', lowercase=True)
    
    X_train_features = self.feature_extraction.fit_transform(X_train)
    Y_train = Y_train.astype('int')
    
    self.model = LogisticRegression()
    self.model.fit(X_train_features, Y_train)
    
    joblib.dump(self.model, self.model_path)

  def is_spam(self, review):
      review = [review]
      input_features = self.feature_extraction.transform(review)
      prediction = self.model.predict(input_features)
      return False if prediction[0] == 1 else True