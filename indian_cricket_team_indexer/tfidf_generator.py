from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd

df = pd.DataFrame("swastik.csv")

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['content'])
cs = cosine_similarity(tfidf_matrix, tfidf_matrix)

with open('tfidf_index.pkl', 'wb') as f:
    pickle.dump((tfidf_vectorizer, tfidf_matrix), f)

with open('cosine_similarity.pkl', 'wb') as f:
    pickle.dump(cs, f)