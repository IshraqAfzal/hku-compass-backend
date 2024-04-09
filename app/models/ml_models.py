import nltk
from .uba.model import UBA
from .sentiment_analysis.model import SentimentAnalysis
from .relevance_analysis.model import RelevanceAnalysis
from .spam_detection.model import SpamDetection
from .transcript_parser.parser import extract_transcript_info


class MLModels():
  def __init__(self) -> None:
    self.setup()
    self.uba = UBA()
    self.spam = SpamDetection()
    self.sentiment = SentimentAnalysis()
    self.relevance = RelevanceAnalysis(self.sentiment)
    self.transcript_parser = extract_transcript_info

  def setup(self):
    nltk.download('all')