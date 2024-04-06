from transformers import AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax
import ssl

class SentimentAnalysis():
  def __init__(self) -> None:
    self.model_name = "cardiffnlp/twitter-roberta-base-sentiment"
    self.load_model_and_tokenizer()

  def load_model_and_tokenizer(self):
      try:
          _create_unverified_https_context = ssl._create_unverified_context
      except AttributeError:
          pass
      else:
          ssl._create_default_https_context = _create_unverified_https_context

      self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
      self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)

  def get_sentiment_scores(self, text):
      encoded_text = self.tokenizer(text, return_tensors='pt')
      output = self.model(**encoded_text)
      scores = output[0][0].detach().numpy()
      scores = softmax(scores)
      scores_dict = {
          'roberta_neg': scores[0],
          'roberta_neu': scores[1],
          'roberta_pos': scores[2]
      }
      return scores_dict