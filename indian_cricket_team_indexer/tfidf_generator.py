from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd

df = pd.read_csv("C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/indian_cricket_team_crawler/webpage_records.csv")

df = df['content'].tolist()

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

with open('C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/indian_cricket_team_processor/tfidf_index.pkl', 'wb') as f:
    pickle.dump((tfidf_vectorizer, tfidf_matrix), f)

with open('C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/indian_cricket_team_processor/cosine_similarity.pkl', 'wb') as f:
    pickle.dump(cosine_similarities, f)