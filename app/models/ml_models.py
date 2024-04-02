from ..logs.logger import logger
from transformers import BertTokenizer, BertModel, AutoModelForSequenceClassification, AutoTokenizer
import nltk, ssl, spacy
from .relevance import description_relevance, action_verbs_count, length as rm_length, roberta_polarity_scores

class MLModels:
  def __init__(self):
    self.setup_models()

  def setup_bert_base_uncased(self):
    model_name = "bert-base-uncased"
    model = BertModel.from_pretrained(model_name)
    self.bert_tokenizer = BertTokenizer.from_pretrained(model_name)
    self.bert_base_uncased_model = model

  def setup_roberta(self):
    try:
      _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    self.roberta_tokenizer = AutoTokenizer.from_pretrained(MODEL)
    self.roberta_model = AutoModelForSequenceClassification.from_pretrained(MODEL)

  def setup_nlp(self):
    self.nlp = spacy.load("en_core_web_sm")

  def setup_models(self):
    # nltk.download('all')
    self.setup_bert_base_uncased()
    self.setup_roberta()
    self.setup_nlp()

  def relevance_score(self, description, text):
    return description_relevance(self.bert_base_uncased_model, self.bert_tokenizer, description, text) + action_verbs_count(self.nlp, text) + rm_length(text) + roberta_polarity_scores(self.roberta_model, self.roberta_tokenizer, text)

  def sort_list_relevance(self, course_description, course_reviews):
    relevance_scores = {}    
    for review in course_reviews:
      score = self.relevance_score(course_description, review)
      relevance_scores[review] = score
    relevance_scores = dict(sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True))
    ret = []
    for key, value in relevance_scores.items():
      ret.append(key)
    return ret

  def sentiment_score(self, text):
    return roberta_polarity_scores(self.roberta_model, self.roberta_tokenizer, text)




