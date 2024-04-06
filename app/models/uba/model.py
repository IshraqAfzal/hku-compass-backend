import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

class UBA():
  def __init__(self) -> None:
    pass

  def give_recommendations(self, title, courses):
    overviews = [course['overview'] for course in courses]
    
    # Vectorize the course overviews
    tfv = TfidfVectorizer(min_df=3, max_features=None,
                          strip_accents='unicode', analyzer='word',
                          token_pattern=r'\w{1,}',
                          ngram_range=(1, 3),
                          stop_words='english')
    tfv_matrix = tfv.fit_transform(overviews)
    
    # Compute sigmoid kernel
    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

    # Map course titles to their indices
    indices = {course['title']: idx for idx, course in enumerate(courses)}

    # Get index of the input course title
    idx = indices[title]

    # Get sigmoid scores for courses
    sig_scores = list(enumerate(sig[idx]))
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:6]  # Exclude the input course itself
    course_indices = [i[0] for i in sig_scores]
    recommended_courses = [courses[i]['title'] for i in course_indices]

    return recommended_courses


