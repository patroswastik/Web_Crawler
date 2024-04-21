from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import pandas as pd
from configparser import ConfigParser

# df = pd.read_csv("C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/indian_cricket_team_crawler/webpage_records.csv")
# df = pd.read_csv("C:/Users/swast/Desktop/MyProjects/python/Web_Crawler/webpage_records.csv")
config = ConfigParser()
config.read("config.ini")
df = pd.read_json(config.get("filepaths", "json_file"))

df = df['content'].values

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

with open(config.get("filepaths", "tfidf_index"), 'wb') as f:
    pickle.dump((tfidf_vectorizer, tfidf_matrix), f)

with open(config.get("filepaths", "consine_similarity"), 'wb') as f:
    pickle.dump(cosine_similarities, f)