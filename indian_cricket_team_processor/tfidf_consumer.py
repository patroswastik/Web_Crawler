from configparser import ConfigParser
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_indexed_data(tfidf_index_file):
    with open(tfidf_index_file, 'rb') as f:
        tfidf_vectorizer, tfidf_matrix = pickle.load(f)

    return tfidf_vectorizer, tfidf_matrix

def search(query, tfidf_vectorizer, tfidf_matrix, documents, top_k):
    query_vector = tfidf_vectorizer.transform([query])

    query_cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)

    most_similar_indices = query_cosine_similarities.argsort()[0][::-1]

    results = []
    for idx in most_similar_indices[:top_k]:
        similarity_score = query_cosine_similarities[0][idx]
        document = documents.iloc[idx]['content']
        title = documents.iloc[idx]['title']
        docId = str(idx)
        results.append((title, similarity_score, document, docId))

    return results

def search_query(query, top_k=5):
    config = ConfigParser()
    config.read("C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/config.ini")
    tfidf_index_file = config.get("filepaths", "tfidf_index")
    json_file = config.get("filepaths", "json_file")

    tfidf_vectorizer, tfidf_matrix = load_indexed_data(
        tfidf_index_file)

    df_documents = pd.read_json(json_file)

    results = search(query, tfidf_vectorizer, tfidf_matrix, df_documents, top_k=top_k)

    return results