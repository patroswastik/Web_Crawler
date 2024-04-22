from configparser import ConfigParser
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_indexed_data(tfidf_index_file, cosine_similarities_file):
    # Load TF-IDF vectorizer and matrix
    with open(tfidf_index_file, 'rb') as f:
        tfidf_vectorizer, tfidf_matrix = pickle.load(f)

    # Load cosine similarities
    with open(cosine_similarities_file, 'rb') as f:
        cosine_similarities = pickle.load(f)

    return tfidf_vectorizer, tfidf_matrix, cosine_similarities

def search(query, tfidf_vectorizer, tfidf_matrix, cosine_similarities, documents, top_k):
    # Vectorize query
    query_vector = tfidf_vectorizer.transform([query])

    # Calculate cosine similarity of query with all documents
    query_cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)

    # Get indices of most similar documents
    most_similar_indices = query_cosine_similarities.argsort()[0][::-1]

    # Display most similar documents
    results = []
    for idx in most_similar_indices[:top_k]:
        similarity_score = query_cosine_similarities[0][idx]
        document = documents.iloc[idx]['content']
        title = documents.iloc[idx]['title']
        results.append((title, similarity_score, document))

    return results

def search_query(query):
    config = ConfigParser()
    config.read("C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/config.ini")
    tfidf_index_file = config.get("filepaths", "tfidf_index")
    cosine_similarities_file = config.get("filepaths", "consine_similarity")
    # csv_file = 'C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/indian_cricket_team_crawler/webpage_records.csv'
    # csv_file = 'C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/webpage_records.csv'
    json_file = config.get("filepaths", "json_file")

    # Load indexed data
    tfidf_vectorizer, tfidf_matrix, cosine_similarities = load_indexed_data(
        tfidf_index_file, cosine_similarities_file)

    # Load documents from json
    df_documents = pd.read_json(json_file)

    # Example: Perform search
    results = search(query, tfidf_vectorizer, tfidf_matrix, cosine_similarities, df_documents, top_k=5)

    return results

# if __name__ == "__main__":
#     tfidf_index_file = 'tfidf_index.pkl'
#     cosine_similarities_file = 'cosine_similarity.pkl'
#     csv_file = 'output.csv'

#     # Load indexed data
#     tfidf_vectorizer, tfidf_matrix, cosine_similarities = load_indexed_data(
#         tfidf_index_file, cosine_similarities_file)

#     # Load documents from CSV
#     df_documents = pd.read_csv(csv_file)

#     # Example: Perform search
#     query = "Virat Kohli"
#     results = search(query, tfidf_vectorizer, tfidf_matrix, cosine_similarities, df_documents, top_k=5)

#     print("Search Results:")
#     for score, document in results:
#         if score == 0:
#             break
#         print(f"Similarity Score: {score:.4f} - Document: {document}")
