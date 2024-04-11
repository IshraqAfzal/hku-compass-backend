import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

class UBA():
  def __init__(self, db) -> None:
    self.db = db

  def give_recommendations(self, title, number):
    courses = self.db.find_all('courses')
    overviews = [course['COURSE_DESCRIPTION'] for course in courses]
    tfv = TfidfVectorizer(min_df=3, max_features=None,
                          strip_accents='unicode', analyzer='word',
                          token_pattern=r'\w{1,}',
                          ngram_range=(1, 3),
                          stop_words='english')
    tfv_matrix = tfv.fit_transform(overviews)
    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
    indices = {course['COURSE_TITLE']: idx for idx, course in enumerate(courses)}
    idx = indices[title]
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:number] if number < len(sig_scores) else sig_scores  # Exclude the input course itself
    course_indices = [i[0] for i in sig_scores]
    recommended_courses = [courses[i] for i in course_indices]

    return recommended_courses


