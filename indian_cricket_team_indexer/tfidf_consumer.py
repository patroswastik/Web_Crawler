import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.DataFrame("")

with open('tfidf_index.pkl', 'rb') as f:
    tfidf_vectorizer, tfidf_matrix = pickle.load(f)

with open('cosine_similarity.pkl', 'rb') as f:
    cosine_similarities = pickle.load(f)

query = "This is a new document."
query_vector = tfidf_vectorizer.transform([query])

query_cosine_similarities = cosine_similarities(query_vector, tfidf_matrix)

most_similar_indices = query_cosine_similarities.argsort()[0][::-1]

for idx in most_similar_indices:
    print(f"Similarity: {query_cosine_similarities[0][idx]}")
    print(f"Document: {df[idx]}")
    print("---")